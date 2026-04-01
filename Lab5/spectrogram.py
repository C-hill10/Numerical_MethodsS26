from windowing import hann
import numpy as np
import matplotlib.pyplot as plt
import CooleyTukey
import sounddevice as sd
import scipy.interpolate 
fs=44100
seconds=3 # 4 seconds does not work, get the edge case data, 1 second does work
if __name__ == "__main__":
    # Generate a sample noise signal
    t = np.arange(0.0, 20.5, 0.02) #changed to 05 instead of 0005
    s1 = np.sin(2*np.pi*t)
    s2 = 2*np.sin(2*np.pi*3*t)
    s2[t <= 10] = s2[12 <= t] = 0
    noise = 0.01*np.random.random(size=len(t))
    x = s1 + s2 + noise
    print(f"x and t shape {x.shape}, {t.shape}")
    t2=np.arange(0.0, 20.5, 0.01)
    # x=np.arange(0.0,3,1/44100)
    # TODO: This does work, just be careful with time you sample
    # print(f"starting recording for {seconds} seconds")
    # x=sd.rec((int(seconds * fs)),samplerate=fs,channels=1)
    # sd.wait()
    # Iterate over the windowed audio and compute power spectrum data
    psds = []
    N = 1024 # samples per chunk of windowed audio
    for chunk in hann(x, N):
        # Compute the fast Fourier transform (FFT) of this chunk
        X = CooleyTukey.FFT2(chunk)[0:N//2] # TODO: Completed
        # Compute the power spectral density (PSD) of this chunk
        # PSD is 10*log10 of the square of the real part of the FFT
        psd = 10*np.log10(np.abs(X)**2)
        psds.append(psd)
    psds = np.array(psds).transpose()

    # Plot the PSDs as a spectrogram
    # TODO: Add a subplot showing the interpolated audio waveform (with shared x-axis)
    # TODO: Label and correct the x-axis and y-axis values
    interpolation=scipy.interpolate.CubicSpline(t,x,bc_type="natural")
    my_spline=CooleyTukey.CubicSpline(t,x) #this worked for small data values, but i got a memory error for trying to hold the whole spline
    fig,(ax0,ax1)=plt.subplots(2,1,sharex=True,gridspec_kw={'height_ratios':[1,2]})
    #ax0.plot(t,x)
    ax0.plot(t2,CooleyTukey.interpolate(my_spline,t2,t,0.02))
    #ax[0].title.set_text("Interpolated waveform")
    ax0.set_ylabel("magnitude")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("power spectral density W/Hz")
    ax1=plt.imshow(psds, aspect='auto', origin='lower')
    
    #ax[1].title.set_text("Power spectral density")
    plt.show()
