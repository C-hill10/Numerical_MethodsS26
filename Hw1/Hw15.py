import matplotlib.pyplot as plt
import numpy as np
import math
# my F(x) will be theta^3 -9 -3sin(theta)-cos(theta)
def derive(x):
    return 3*x**2-3*np.cos(x)+np.sin(x)
def func(x):
    return x**3 -9 -3*np.sin(x)-np.cos(x)
def bisection(a,b):
    done=False
    while not done:
        xm=(a+b)/2
        bisectionlist.append(xm)
        result=func(xm)
        if abs(b-a)<1e-8:
            return xm
            done=True
        else:
            if (func(a))*(result) >0:
                a=xm
            else:
                b=xm
def secant(x0,x1):
    done =False
    while not done:
        x2=x1-func(x1)*(x1-x0)/(func(x1)-func(x0))
        secantlist.append(x2)
        if abs(x2-x1)<=1e-8:
            return x2
        else:
            x0=x1
            x1=x2
def RF(a,b):
    done=False
    while not done:
        xr= (a*(func(b))-b*(func(a)))/((func(b))-(func(a)))
        rflist.append(xr)
        if abs(b-a)<1e-4:
            return xr
        else:
            if (func(a))*(func(xr)) >0:
                a=xr
            else:
                b=xr
    
if __name__=="__main__":
    x=np.arange(-10,10,1)
    plt.plot(x,func(x))
    plt.grid()
    plt.show()
    #based on plot, guess around 2.2 for solution, bounds at 2 and 2.5 for bisection
    done=False
    guess1=2.5
    guess1new=0
    nrlist=[]
    nrlist.append(guess1)
    rflist=[]
    bisectionlist=[]
    secantlist=[]
    while not done:
        guess1new=guess1-func(guess1)/(derive(guess1))
        nrlist.append(guess1new)
        if abs(guess1new-guess1)<=1e-8:
            done=True
        else:
            guess1=guess1new
    bisectionguess=bisection(2,2.5)
    rfguess=RF(2,2.5)
    secantguess=secant(2,2.5)
    plt.plot(nrlist,label="Newton-Raphson",linestyle=":")
    plt.plot(bisectionlist,label="Bisection",linestyle="--")
    plt.plot(secantlist,label="Secant",linestyle="-.")
    plt.plot(rflist,label="Regula Falsi",linestyle=":")
    plt.legend(loc="upper right")
    plt.show()
