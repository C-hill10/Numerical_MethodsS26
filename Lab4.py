import matplotlib.pyplot as plt
import numpy as np
import math
def bisect(func,a,b,tol):
    while abs(a-b)>tol:
        xm=(a+b)/2
        result=func(xm)
        if result*func(a)>0:
            a=xm
        else:
            b=xm
        yield xm
def regula_falsi(func,a,b,tol):
    while abs(a-b)>tol:
        xr=(a*func(b)-b*func(a))/(func(b)-func(a))
        result=func(xr)
        if result*func(a)>0:
            a=xr
        else:
            b=xr
        yield xr
def fixed_point(func,x,tol):
    x1=func(x)
    while abs(x-x1)>tol:
        x=x1
        yield x
def nr(func,x,tol,derivative):
    x1=x-(func(x)/derivative(x))
    while abs(x-x1) > tol:
        x=x1
        yield x
def secant(func,x,x1,tol):
    while abs(x-x1)>tol:
        x2=x1-func(x1)*(x1-x)/(func(x1)-func(x))
        x=x1
        x1=x2
        yield x2
def golden_section(func,a,b,epsilon):
    phi = (math.sqrt(5)+1)/2
    while abs(a-b)>epsilon:
        x1=b-(b-a)/phi
        x2=a+(b-a)/phi
        if func(x1)<func(x2):
            a=x1
        else:
            b=x2
        yield (a+b)/2    
def parabolic_interpolation(func,a,b,c,limit):
    for counter in range(0,limit):
        #attempt from textbook
        numerator=(((b-a)**2)*(func(b)*func(c)))-(((b-c)**2) *(func(b)-func(a)))
        denominator=((b-a)*(func(b)*func(c)))-((b-c)*(func(b)-func(a)))
        x=b-(1/2)*(numerator/denominator)
        if b<x and x<c:
            if negfunc(x)<negfunc(b):
                a,b=b,x
            else:
                c=x
        else:
            if negfunc(x)<negfunc(b):
                c,b=b,x
            else:
                a=x
        yield x

def error(solution,func,method,*args,**kwargs):
    # kwargs are plot_error and plot_convergence (bools)
    x=method(func,*args)
    guesses=list(x)
    error=[]
    for answer in guesses:
        error.append(abs(answer-solution))
    if bool(kwargs["plot_error"]):
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        line,=ax.plot(error,color='blue')
        ax.set_yscale('log')
        plt.grid()
        plt.title("Plot of absolute error vs iteration")
        plt.show(block=False)
    nextlist=guesses[1:]
    guesses=guesses[:-1]
    print(guesses)
    print(nextlist)
    if bool(kwargs['plot_convergence']):
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        plt.scatter(guesses,nextlist)
        plt.plot(guesses,nextlist,marker="o")
        ax.set_yscale('log')
        plt.title("Plot of convergence")
        plt.grid()
        plt.show(block=True)
    return len(np.polyfit(guesses,nextlist,1)-1)

if __name__=="__main__":
    func=lambda x: np.sin(x)
    deg = error(0,func,bisect,-2,1,1e-5,plot_error=True,plot_convergence=True)
    print(f"convergence degree is {deg}")