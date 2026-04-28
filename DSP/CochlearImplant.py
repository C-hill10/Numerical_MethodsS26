import numpy as np
import wave
import sounddevice as sd
import matplotlib.pyplot as plt
import scipy
def findBW(num_channels):
    speech_channels=round((num_channels*6/10),0)
    other_channels=num_channels-speech_channels
    speechbw=900/speech_channels
    otherbw=3000/other_channels
    bwArray=np.zeros(shape=(num_channels,))
    for i in range(0,num_channels):
        if i<speech_channels:
            bwArray[i]=speechbw
        else:
            bwArray[i]=otherbw
    return (speechbw,otherbw,bwArray)

if __name__=="__main__":
    fs=44100
    speechbw,otherbw,bwArray=findBW(8)
    try:
        music_file=wave.open("../FinalProject/GGST-Jam_verse.wav","rb")
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
            seconds=np.arange(0,udio_int.shape[0]/fs,1/fs)
            # fig,ax=plt.subplots()
            # plt.plot(seconds,udio_int[::,0],seconds,udio_int[::,1])
            # plt.xlabel("seconds")
            # plt.ylabel("16 bit PCM Value from Wav file")
            # plt.show()
            rectangular_window=np.ones((2048,))
            my_stft=scipy.signal.ShortTimeFFT(rectangular_window,100,fs)
            right_channel=my_stft.stft(udio_int[::,0])
            print(right_channel.shape)
            left_channel=my_stft.stft(udio_int[::,1])