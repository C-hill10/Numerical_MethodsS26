import matplotlib.pyplot as plt
import numpy as np
import math
def bisection1(a,b):
    done=False
    while not done:
        xm=(a+b)/2
        result=np.sin(xm)-xm**2
        if abs(b-a)<1e-8:
            return xm
            done=True
        else:
            if (np.sin(a)-(a**2))*(result) >0:
                a=xm
            else:
                b=xm
if __name__=="__main__":
    x=np.arange(-1,1.2,0.01)
    plt.plot(x,(np.sin(x)-x**2))
    plt.grid()
    plt.show()
    #based on plot, zeros at 0 and around .75
    #brackets at -0.1 and 0.1, and .7 to .9
    result1=bisection1(-0.1,0.1)
    result2=bisection1(0.7,1)
    print(f"root 1 is {result1} bounds started -0.1 and 0.1")
    print(f"root 2 is {result2} bounds started 0.7 and 0.8")