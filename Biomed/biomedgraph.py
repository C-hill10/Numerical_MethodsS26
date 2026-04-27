import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.io


if __name__=="__main__":
    data=scipy.io.loadmat("rawdata.mat")
    print(data.keys())
    data=np.array(data["data_raw"])
    print(data.shape)
    print(data[0][0][::])
    data=data.reshape((512,4096))
    print(data.shape)
    print(data[0][::])
    data=data.transpose()
    print(data.shape)
    fig, ax = plt.subplots()
    img=ax.imshow(data,extent=[0,3.2,0,2.5],cmap="RdBu",norm=matplotlib.colors.LogNorm())
    ax.set_aspect("auto")
    plt.colorbar(img)
    plt.xlabel("Lateral position (mm)")
    plt.ylabel("Axal (depth) position (mm)")
    plt.show()