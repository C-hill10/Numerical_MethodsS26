import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.io


if __name__=="__main__":
    data=scipy.io.loadmat("rawdata.mat")
    data=np.array(data["data_raw"])
    data=data.reshape((512,4096))
    data=data.transpose()
    print(data.shape)
    fig, ax = plt.subplots()
    img=ax.imshow(data,extent=[0,3.2,0,2.5],cmap="RdBu",norm=matplotlib.colors.LogNorm())
    ax.set_aspect("auto")
    plt.colorbar(img)
    rectangular_window128=np.ones((1,128))
    my_stft=scipy.signal.ShortTimeFFT(rectangular_window128,128,1/262144)
    test=my_stft(data[::,0])
    plt.xlabel("Lateral position (mm)")
    plt.ylabel("Axal (depth) position (mm)")
    plt.show()