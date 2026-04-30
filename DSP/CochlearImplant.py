import numpy as np
import math
import wave
import sounddevice as sd
import matplotlib.pyplot as plt
import scipy
def findBW(num_channels):
    speech_channels=round((num_channels*6/10),0)
    other_channels=num_channels-speech_channels
    speechbw=900/speech_channels
    otherbw=3000/other_channels
    print()
    bwArray=np.zeros(shape=(num_channels,))
    for i in range(0,num_channels):
        if i<speech_channels:
            bwArray[i]=speechbw
        else:
            bwArray[i]=otherbw
    return (speechbw,otherbw,bwArray)

if __name__=="__main__":
    fs=44100
    num_channels=16
    frequencystep=np.linspace(0,fs,2048)
    #from testing earlier, each entry represents ~22Hz of BW, 180 steps to get to 4kHz
    speechbw,otherbw,bwArray=findBW(num_channels)
    print(bwArray)
    try:
        music_file=wave.open("./Dna-More_singing.wav","rb")
    except FileNotFoundError:
        print("Error: file does not exist")
    else:
        with music_file:
            nchannels = music_file.getnchannels()    # Number of channels (1=mono, 2=stereo)  
            sampwidth = music_file.getsampwidth()    # Bytes per sample (e.g., 2 for 16-bit)  
            framerate = music_file.getframerate()    # Sample rate (Hz)  
            nframes = music_file.getnframes()        # Total samples  
            comptype = music_file.getcomptype()      # Compression type (usually "NONE" for PCM)  
            compname = music_file.getcompname()      # Compression name  
            raw_data=music_file.readframes(nframes)
            if sampwidth==1:
                dtype=np.uint8
                print(f"Dtype is 8 bits")
            elif sampwidth == 2:  
                dtype = np.int16 
                print(f"Dtype is 16 bits") 
            elif sampwidth == 4:  
                dtype = np.int32  # Assumes 32-bit integer (common for PCM) 
                print(f"Dtype is 32 bits") 
            else:  
                raise ValueError(f"Unsupported sample width: {sampwidth} bytes")  
            
            audio_int = np.frombuffer(raw_data, dtype=dtype)  # Integer array   
            udio_int = audio_int.reshape(-1, nchannels)  # Shape: (nframes, nchannels) 
            print(f"shape of original data file is {udio_int.shape}")
            seconds=np.arange(0,udio_int.shape[0]/fs,1/fs)
            window=scipy.signal.windows.hamming(2048,sym=False)
            my_stft=scipy.signal.ShortTimeFFT(window,100,fs,fft_mode="twosided")
            right_channel=my_stft.stft(udio_int[::,0])
            left_channel=my_stft.stft(udio_int[::,1])
            channel_values_r=np.zeros(shape=(right_channel.shape),dtype=complex)
            channel_values_l=np.zeros(shape=(right_channel.shape),dtype=complex)
            sd.play(udio_int)
            sd.wait()
            #spectro_db= 10 * np.log10(np.fmax(right_spectro, 1e-4))  # limit range to -40 dB
            for i in range(0,right_channel.shape[1]):
                current_index=0
                channel_index=0
                bwUsed=0
                channelmag=0
                for j in range(0,188): #amount of frequency steps until we hit 4kHz
                    bwUsed+=frequencystep[1]
                    channelmag+=right_channel[j][i]
                    if channel_index<=(num_channels-1) and bwUsed>=bwArray[channel_index]:
                        channel_values_r[current_index:j,i]=channelmag
                        channel_index+=1
                        current_index=j
                        bwUsed=0
                        channelmag=0
                if j==187 and current_index!=j:
                    channel_values_r[current_index:j,i]=channelmag
            for i in range(0,right_channel.shape[1]): #run it back for the left channel i should've made this a function
                current_index=0
                channel_index=0
                bwUsed=0
                channelmag=0
                for j in range(5,187): #amount of frequency steps until we hit 4kHz
                    bwUsed+=frequencystep[1]
                    channelmag+=right_channel[j][i]
                    if channel_index<=num_channels-1 and (bwUsed>=bwArray[channel_index]
                     or (bwArray[channel_index]-bwUsed)<(frequencystep[1])/2):
                        channel_values_l[current_index:j,i]=channelmag
                        channel_index+=1
                        current_index=j
                        bwUsed=0
                        channelmag=0
                    if j==187 and current_index!=j:
                        channel_values_l[current_index:j,i]=channelmag
            adjusted_right=my_stft.istft(channel_values_r)
            img=plt.imshow(10*np.log10(np.abs(channel_values_r[0:180,::])**2),cmap="inferno"
            ,aspect="auto",extent=[0,1,frequencystep[1]*180,0])
            plt.colorbar(img)
            plt.show()
            print(adjusted_right.shape)
            adjusted_left=my_stft.istft(channel_values_l)
            processed_song=np.zeros(shape=(adjusted_right.shape[0],2))
            processed_song[::,0]=adjusted_right
            processed_song[::,1]=adjusted_left
            processed_song=processed_song*(1/1e5)
            scipy.io.wavfile.write("8channelDna.wav",fs,(processed_song*5e4).astype(np.int16))
            sd.play(processed_song)
            sd.wait()