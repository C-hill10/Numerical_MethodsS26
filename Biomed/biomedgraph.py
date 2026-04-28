import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.io


if __name__=="__main__":
    fs=262144
    data=scipy.io.loadmat("rawdata.mat")
    data=np.array(data["data_raw"])
    data=data.reshape((512,4096))
    post_stft=np.zeros(shape=(512,128,33))
    data=data.transpose()
    test=np.array([[1,2]]) #shape is 1,2 and prints 1 row 2 columns 
    print(data.shape)
    fig, ax = plt.subplots()
    # img=ax.imshow(data,extent=[0,3.2,0,2.5],cmap="RdBu",norm=matplotlib.colors.LogNorm())
    # ax.set_aspect("auto")
    # plt.colorbar(img)
    rectangular_window=np.ones((128,))
    my_stft=scipy.signal.ShortTimeFFT(rectangular_window,128,1/fs,fft_mode="twosided")
    for i in range(0,512):
        test=my_stft.stft(data[::,i],axis=0)
        post_stft[i]=test
    print(test.shape)
    #test=test.reshape(4096,512)
    power=np.multiply(post_stft,np.conjugate(post_stft))
    print(power.shape)
    #do the weighted centroid thing
    for j in range(0,512):
        for index in range(0,3):
            for i in range(0,128):
                frequency= i*fs/(1024*2*math.pi)
                freqtime=frequency*power[j][i][index]
    # img=ax.imshow(np.abs(inverse),extent=[0,3.2,0,2.5],cmap="RdBu")
    # plt.xlabel("Lateral position (mm)")
    # plt.ylabel("Axal (depth) position (mm)")
    # ax.set_aspect("auto")
    # plt.colorbar(img)
    # plt.show()