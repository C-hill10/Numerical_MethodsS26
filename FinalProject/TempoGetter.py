import numpy as np
import math
import wave
import matplotlib.pyplot as plt
import sounddevice as sd
import argparse
import scipy
import librosa
import libfmp
import cmath
#using this site for reading wav file into np array https://www.w3reference.com/blog/python-write-a-wav-file-into-numpy-float-array/
#using these from a stack exchange thread https://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units
#my own FFT from lab 4
def FFT2(sequence):
    N=len(sequence)
    if not( (N & (N-1) == 0) and N != 0):
        raise ValueError("number is not a power of 2")
    if N==1:
        return sequence
    omega=cmath.exp(-2*math.pi*1j/N)
    even,odd=sequence[0::2],sequence[1::2]
    y_even,y_odd=FFT2(even),FFT2(odd)
    y_current=np.zeros(shape=(N,),dtype='complex')
    for j in range(0,N//2):
        y_current[j]=y_even[j]+(omega**j)*y_odd[j]
        y_current[j+N//2]=y_even[j]-(omega**j)*y_odd[j]
    return y_current
def butter_lowpass(cutoff, fs, order=5):
    return scipy.signal.butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = scipy.signal.lfilter(b, a, data)
    return y
def my_stft(signal,num_samples,Hop,window_length,window):
    stft_out=np.zeros(shape=(num_samples//2+1,signal.shape[0]//hop+1),dtype=complex)
    index=0
    window=scipy.signal.windows.hann(window_length,sym=False)
    for i in range(0,stft_out.shape[1]):
        stft_out[::,index]=FFT2(np.multiply(signal[index:index+num_samples],window))
        index+=Hop
    return stft_out

#copied functions i needed in from https://meinardmueller.github.io/libfmp and modified them
#also https://www.audiolabs-erlangen.de/resources/MIR/FMP/C6/C6S2_TempogramFourier.html
def compute_local_average(x, M):
    """Compute local average of signal

    Notebook: C6/C6S1_NoveltySpectral.ipynb

    Args:
        x (np.ndarray): Signal
        M (int): Determines size (2M+1) in samples of centric window  used for local average

    Returns:
        local_average (np.ndarray): Local average signal
    """
    L = len(x)
    local_average = np.zeros(L)
    for m in range(L):
        a = max(m - M, 0)
        b = min(m + M + 1, L)
        local_average[m] = (1 / (2 * M + 1)) * np.sum(x[a:b])
    return local_average

def compute_novelty_spectrum(x, Fs=1, N=1024, H=256, gamma=100.0, M=10, norm=True):
    """Compute spectral-based novelty function

    Notebook: C6/C6S1_NoveltySpectral.ipynb

    Args:
        x (np.ndarray): Signal
        Fs (scalar): Sampling rate (Default value = 1)
        N (int): Window size (Default value = 1024)
        H (int): Hop size (Default value = 256)
        gamma (float): Parameter for logarithmic compression (Default value = 100.0)
        M (int): Size (frames) of local average (Default value = 10)
        norm (bool): Apply max norm (if norm==True) (Default value = True)

    Returns:
        novelty_spectrum (np.ndarray): Energy-based novelty function
        Fs_feature (scalar): Feature rate
    """
    print(f'Library STFT took parameters shape of input {x.shape} num samples={N}, hop {H}, Window len {N}')
    X = librosa.stft(x, n_fft=N, hop_length=H, win_length=N, window='hann')
    print(f'after doing library stft, get an output with shape {X.shape}')
    #testing my STFT

    Fs_feature = Fs / H
    Y = np.log(1 + gamma * np.abs(X))
    Y_diff = np.diff(Y)
    Y_diff[Y_diff < 0] = 0
    novelty_spectrum = np.sum(Y_diff, axis=0)
    novelty_spectrum = np.concatenate((novelty_spectrum, np.array([0.0])))
    if M > 0:
        local_average = compute_local_average(novelty_spectrum, M)
        novelty_spectrum = novelty_spectrum - local_average
        novelty_spectrum[novelty_spectrum < 0] = 0.0
    if norm:
        max_value = max(novelty_spectrum)
        if max_value > 0:
            novelty_spectrum = novelty_spectrum / max_value
    return novelty_spectrum, Fs_feature
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
def resample_signal(x_in, Fs_in, Fs_out=100, norm=True, time_max_sec=None, sigma=None):
    """Resample and smooth signal

    Notebook: C6/C6S1_NoveltyComparison.ipynb

    Args:
        x_in (np.ndarray): Input signal
        Fs_in (scalar): Sampling rate of input signal
        Fs_out (scalar): Sampling rate of output signal (Default value = 100)
        norm (bool): Apply max norm (if norm==True) (Default value = True)
        time_max_sec (float): Duration of output signal (given in seconds) (Default value = None)
        sigma (float): Standard deviation for smoothing Gaussian kernel (Default value = None)

    Returns:
        x_out (np.ndarray): Output signal
        Fs_out (scalar): Feature rate of output signal
    """
    if sigma is not None:
        x_in = ndimage.gaussian_filter(x_in, sigma=sigma)
    T_coef_in = np.arange(x_in.shape[0]) / Fs_in
    time_in_max_sec = T_coef_in[-1]
    if time_max_sec is None:
        time_max_sec = time_in_max_sec
    N_out = int(np.ceil(time_max_sec*Fs_out))
    T_coef_out = np.arange(N_out) / Fs_out
    if T_coef_out[-1] > time_in_max_sec:
        x_in = np.append(x_in, [0])
        T_coef_in = np.append(T_coef_in, [T_coef_out[-1]])
    x_out = scipy.interpolate.interp1d(T_coef_in, x_in, kind='linear')(T_coef_out)
    if norm:
        x_max = max(x_out)
        if x_max > 0:
            x_out = x_out / max(x_out)
    return x_out, Fs_out
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
            nframes = music_file.getnframes()        # Total samples  
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
            fig,ax=plt.subplots(2,1)
            plt.xlabel("seconds") 
            fs=22050
            cutoff=10
            nov_func,fs_nov=compute_novelty_spectrum(udio_int[::,1].astype(float),fs,N=2048,
            H=128,gamma=100,M=10,norm=True)
            fs=100
            #resample function to 200 samples/sec
            resampled_func,fs=resample_signal(nov_func,fs_nov,fs,norm=True,time_max_sec=udio_int.shape[0]/44100)
            print(resampled_func.shape)
            test_tempo=np.arange(50,250,1)
            #print(down_sampled.shape)
            time=np.linspace(0,resampled_func.shape[0]/fs,resampled_func.shape[0])
            picture=tempo_analysis(resampled_func,fs,fs,cutoff,test_tempo)
            ax[0].plot(time,resampled_func)
            img=ax[1].imshow(np.abs(picture).transpose(),cmap="Greys",
            aspect="auto",extent=[0,resampled_func.shape[0]/(fs),test_tempo[-1],test_tempo[0]])
            plt.colorbar(img)
            plt.show()
