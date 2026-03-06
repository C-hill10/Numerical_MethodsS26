import matplotlib.pyplot as plt
import numpy as np
import math
def bisect(func,a,b,tol):
    while abs(a-b)>tol:
        xm=a+b
        result=func(xm)
        if result*func(a)>0:
            a=xm
        else:
            b=xm
        yield xm
def regula_falsi(func,a,b,tol):
    while abs(a-b)>tol:
        xr=(a*func(b)-b*func(a))/(func(b)-func(a))
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
        x2=x1-func(x1)*(x1-x0)/(func(x1)-func(x0))
        x=x1
        x1=x2
        yield x2    

def error(solution,func,method,*args,**kwargs):
    x=method(func,)
