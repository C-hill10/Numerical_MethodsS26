import matplotlib.pyplot as plt
import numpy as np
import math
class ConvergenceError(RuntimeError):
    pass
def bisect(func,a,b,tol):
    limit=50
    counter=0
    while abs(a-b)>tol and counter < limit:
        counter+=1
        if counter>=49:
            raise ConvergenceError("Exceeded iteration limit")
        xm=(a+b)/2
        result=func(xm)
        if result*func(a)>0:
            a=xm
        else:
            b=xm
        yield xm
def regula_falsi(func,a,b,tol):
    limit=50
    counter=0
    while abs(a-b)>tol:
        counter+=1
        if counter>=49:
            raise ConvergenceError("Exceeded global iteration limit")
        xr=(a*func(b)-b*func(a))/(func(b)-func(a))
        result=func(xr)
        if result*func(a)>0:
            a=xr
        else:
            b=xr
        yield xr
def fixed_point(func,x,tol):
    limit=50
    counter=0
    x1=func(x)
    while abs(x-x1)>tol:
        if counter>=limit:
            raise ConvergenceError("exceeded global iteration limit")
        yield x
        x=x1
        x1=func(x)
        counter+=1
def nr(func,x,tol,derivative):
    limit=50
    counter=0
    x1=x-(func(x)/derivative(x))
    while abs(x-x1) > tol:
        if counter>=limit:
            raise ConvergenceError("exceeded global iteration limit")
        yield x
        x=x1
        x1=x-(func(x)/derivative(x))
        counter+=1
def secant(func,x,x1,tol):
    limit=50
    counter=0
    while abs(x-x1)>tol:
        if counter>=limit:
                raise ConvergenceError("exceeded global iteration limit")
        yield x
        x2=x1-func(x1)*(x1-x)/(func(x1)-func(x))
        x=x1
        x1=x2
        counter+=1
def golden_section(func,a,b,epsilon):
    limit=50
    counter=0
    phi = (math.sqrt(5)+1)/2
    while abs(a-b)>epsilon:
        if counter>=limit:
                raise ConvergenceError("exceeded global iteration limit")
        x1=b-(b-a)/phi
        x2=a+(b-a)/phi
        if func(x1)<func(x2):
            a=x1
        else:
            b=x2
        yield (a+b)/2 
        counter+=1   
def parabolic_interpolation(func,a,b,c,limit):
    for counter in range(0,limit):
        if counter>=limit:
                raise ConvergenceError("exceeded global iteration limit")
        numerator=(((b-a)**2)*(func(b)*func(c)))-(((b-c)**2) *(func(b)-func(a)))
        denominator=((b-a)*(func(b)*func(c)))-((b-c)*(func(b)-func(a)))
        x=b-(1/2)*(numerator/denominator)
        if b<x and x<c:
            if func(x)<func(b):
                a,b=b,x
            else:
                c=x
        else:
            if func(x)<func(b):
                c,b=b,x
            else:
                a=x
        yield x
        counter+=1

def error(solution,func,method,*args,**kwargs):
    # kwargs are plot_error and plot_convergence (bools)
    x=method(func,*args)
    guesses=list(x)
    error=[]
    errorlogx=[]
    errorlogy=[]
    for answer in guesses:
        error.append(abs(answer-solution))
    for entry in range(0,len(guesses)-1):
        #Entry in book mentioned formula being related to error and exponential
        #E_n+1=K*(E_n)^p, using log to solve for p with plot fitting
        errorlogx.append(math.log(error[entry]))
        errorlogy.append(math.log(error[entry+1]))

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
    if bool(kwargs['plot_convergence']):
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        plt.scatter(guesses,nextlist)
        plt.plot(guesses,nextlist,marker="o")
        ax.set_yscale('log')
        plt.title("Plot of convergence")
        plt.grid()
        plt.show(block=True)
    return np.polyfit(errorlogx,errorlogy,1)

if __name__=="__main__":
    #Bisection test
    func=lambda x: np.sin(x)
    deg = error(0,func,bisect,-2,1,1e-5,plot_error=False,plot_convergence=0)
    print(f"convergence degree of bisection is {deg[0]}")

    #Regula falsi test with same parameters as bisection
    func=lambda x: np.sin(x)
    deg = error(0,func,regula_falsi,-2,1,1e-5,plot_error=False,plot_convergence=False)
    print(f"convergence degree of Regula falsi is {deg[0]}")

    #newton-raphson testing
    func= lambda x:-0.87*x**2+1.65*x+8.25
    derivative= lambda x: -1.74*x+1.65
    deg=error(4.17038,func,nr,3,1e-8,derivative,plot_error=0,plot_convergence=0)
    print(f"convergence degree of NR is {deg[0]}")
    #secant method test to see if i have it right for order of convergence
    func= lambda x:-0.87*x**2+1.65*x+8.25
    derivative= lambda x: -1.74*x+1.65
    deg=error(4.17038,func,secant,3.5,4.5,1e-8,plot_error=0,plot_convergence=0)
    print(f"convergence degree of Secant is {deg[0]}")
    #Fixed point test, the fixed point is 0
    func=lambda x: x**2
    deg= error(0,func,fixed_point,0.5,1e-3,plot_error=0,plot_convergence=False)
    print(f"convergence degree of fixed point is {deg[0]}")

    #optimization test 
    func= lambda x: (-.3*x**4)+(1.8*x**3)-(1.2*x**2)+2*x
    deg= error(4.1122,func,golden_section,3,5,1e-5,plot_error=0,plot_convergence=False)
    print(f"convergence degree of golden section is {deg[0]}")