import matplotlib.pyplot as plt
import numpy as np
import math
def bisectioncos(a,b):
    done=False
    counter=0
    while not done:
        counter+=1
        xm=(a+b)/2
        result=np.cos(xm)-xm
        if abs(b-a)<1e-4:
            return (xm,counter)
            done=True
        else:
            if (np.cos(a)-(a))*(result) >0:
                a=xm
            else:
                b=xm
def RFcos(a,b):
    done=False
    counter=0
    while not done:
        counter+=1
        xr= (a*(np.cos(b)-b)-b*(np.cos(a)-a))/((np.cos(b)-b)-(np.cos(a)-a))
        if abs(b-a)<1e-4:
            return (xr,counter)
            done=True
        else:
            if (np.cos(a)-(a))*(np.cos(xr)-xr) >0:
                a=xr
            else:
                b=xr
if __name__=="__main__":
    countercos=0
    counterrf=0
    x=np.arange(0,1,0.01)
    print(x)
    plt.plot(x,(np.cos(x)-x))
    plt.grid()
    plt.show()
    result1,countercos=bisectioncos(0.5,1)
    result2,counterrf=RFcos(0.5,1)
    print(f"root 1 is {result1} it took {countercos} iterations")
    print(f"root 2 is {result2} it took {counterrf} iterations")