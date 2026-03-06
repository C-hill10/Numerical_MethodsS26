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

def error(solution,func,method,*args,**kwargs):
    # kwargs are plot_error and plot_convergence (bools)
    print(f'args 0: {args[0]},args 1: {args[1]},args 2: {args[2]} ')
    x=method(func,args[0],args[1],args[2])
    guesses=list(x)
    if bool(kwargs["plot_error"]):
        error=[]
        for answer in guesses:
            error.append(abs(answer-solution))
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        line,=ax.plot(error,color='blue')
        ax.set_yscale('log')
        plt.grid()
        plt.show(block=False)
    if bool(kwargs['plot_convergence']):
        nextlist=guesses[1:]
        guesses=guesses[:-1]
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        line,=ax.plot(guesses,nextlist,color='red')
        ax.set_yscale('log')
        plt.grid()
        plt.show(block=True)
    print(list(x))

if __name__=="__main__":
    func=lambda x: np.sin(x)
    error(0,func,bisect,-2,1,1e-5,plot_error=True,plot_convergence=True)