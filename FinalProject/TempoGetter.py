import numpy as np
import math
import wave
import matplotlib.pyplot as plt
import sounddevice as sd
import argparse
import scipy
#using this site for reading wav file into np array https://www.w3reference.com/blog/python-write-a-wav-file-into-numpy-float-array/

#using these from a stack exchange thread https://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units
def butter_lowpass(cutoff, fs, order=5):
    return scipy.signal.butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = scipy.signal.lfilter(b, a, data)
    return y

def tempo_analysis(data,fs,N,Hop,Theta):
    win = np.hanning(N)
    N_left = N // 2
    L = data.shape[0]
    half_pad = N_left
    L_pad = L + 2*half_pad
    x_pad = np.concatenate((np.zeros(half_pad), data, np.zeros(half_pad)))
    t_pad = np.arange(L_pad)
    M = int(np.floor(L_pad - N) / Hop) + 1
    K = len(Theta)
    X = np.zeros((K, M), dtype=complex)

    for k in range(K):
        omega = (Theta[k] / 60) / fs
        exponential = np.exp(-2 * np.pi * 1j * omega * t_pad)
        x_exp = x_pad * exponential
        for n in range(M):
            t_0 = n * Hop
            t_1 = t_0 + N
            X[k, n] = np.sum(win * x_exp[t_0:t_1])
        T_coef = np.arange(M) * Hop / fs
        F_coef_BPM = Theta
    return X # T_coef, F_coef_BPM

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="reads wav file and outputs a low frequency fourier transform plot to try and guess BPM")
    parser.add_argument('file',type=str)
    args=parser.parse_args()
    try:
        music_file=wave.open(args.file,"rb")
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
            print(udio_int)
            seconds=np.arange(0,udio_int.shape[0]/44100,1/44100)
            fig,ax=plt.subplots()
            #plt.plot(seconds,udio_int[::,0],seconds,udio_int[::,1])
            plt.xlabel("seconds")
            #plt.ylabel("16 bit PCM Value from Wav file")
            #plt.show()
            # if the highest bpm i want to see is 300, that is 5 hz, so i need at least 10 hz of samples,
            # to be safe maybe do 500 samples/sec 
            fs=100
            cutoff=fs//2
            pre_filtered=butter_lowpass_filter(udio_int[::,0],cutoff,44100)
            filter_down=pre_filtered[::44100//fs,]
            #down_sampled=udio_int[::44100//fs,0]
            test_tempo=np.arange(50,250,1)
            #print(down_sampled.shape)
            time=np.linspace(0,filter_down.shape[0]/fs,filter_down.shape[0])
            #filtered_data= butter_lowpass_filter(down_sampled,10,fs)
            picture=tempo_analysis(filter_down,fs,fs,fs//2,test_tempo)
            print(picture.shape)
            img=plt.imshow(np.abs(picture).transpose(),cmap="Greys",
            aspect="auto",extent=[0,filter_down.shape[0]/fs,test_tempo[-1],test_tempo[0]])
            plt.colorbar(img)
            plt.show()
