import numpy as np
import matplotlib.pyplot as plt



if __name__=="__main__":
    time_value=np.arange(0,3+6/30,1/30)
    print(time_value.size)
    data=np.array([0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,4,3,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-6,-8,-8,-8,-8,-8,-8,-8,-9,-10,-10,-10,-10,-10,-10,-10,-10,0,0,0,4,10,15,18,20,20,20,20,20,20,20,20,20,20,20,20,20,10,5,0,-3,-7,-8,-9,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-5,5,10,12,15
])
    stimulus=np.zeros(shape=(96,))
    for entry in range(0,96):
        if entry<=33:
            stimulus[entry]=0
        elif entry<=51:
            stimulus[entry]=-10
        elif entry<=71:
            stimulus[entry]=20
        elif entry<=90:
            stimulus[entry]=-10
        else:
            stimulus[entry]=20  
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(time_value,data,label="collected data",)
    ax.plot(time_value,stimulus,label="stimulus data",linestyle="--",linewidth=2,color="purple")
    attempt=np.polyfit(time_value,data,14)
    attemptfit=np.poly1d(attempt)
    ax.plot(time_value,attemptfit(time_value),label="14th deg polynomial fit",linewidth=3,color="orange")
    ax.legend()
    outputmagnitude=np.abs(np.fft.fft(data))
    stimulusftmagnitude=np.abs(np.fft.fft(stimulus))
    result=np.divide(outputmagnitude,stimulusftmagnitude)
    plt.xlabel("time (seconds)")
    plt.ylabel("angle of eye (degrees)")
    plt.show()
    plt.plot(result)
    #plt.xlim(right=45,left=0)
    plt.show()