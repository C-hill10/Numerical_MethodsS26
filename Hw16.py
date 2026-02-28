import matplotlib.pyplot as plt
import numpy as np
import math
phi = (math.sqrt(5)+1)/2
def func(x):
    return (-.3*x**4)+(1.8*x**3)-(1.2*x**2)+2*x
def negfunc(x):
    return -func(x)
def golden_section(a,b,epsilon):
    while abs(a-b)>epsilon:
        x1=b-(b-a)/phi
        x2=a+(b-a)/phi
        if func(x1)<func(x2):
            a=x1
        else:
            b=x2
    return (a+b)/2
def parabolic_interpolation(a,b,c,limit):
    counter=0
    while counter<limit:
        counter+=1
        xmin=(1/2)*(negfunc(a)*(c**2-b**2)+negfunc(b)*(a**2-c**2)+negfunc(c)*(b**2-a**2))/(negfunc(a)*(c-b)+negfunc(b)*(a-c)+negfunc(c)*(b-a))
        if xmin<b:
            b,c=xmin,b
        else:
            a,b,c=b,xmin,c
    return xmin


if __name__ == "__main__":
    gs_guess=golden_section(-2,4,1e-2)
    print(f"{gs_guess}, value of func here is {func(gs_guess)}")
    paraguess=parabolic_interpolation(1.7,2,2.7,5)
    print(f"{paraguess}, value of func here is {func(paraguess)}")