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
    for counter in range(0,limit):
        #attempt from textbook
        numerator=(((b-a)**2)*(negfunc(b)*negfunc(c)))-(((b-c)**2) *(negfunc(b)-negfunc(a)))
        denominator=((b-a)*(negfunc(b)*negfunc(c)))-((b-c)*(negfunc(b)-negfunc(a)))
        x=b-(1/2)*(numerator/denominator)
        print(f"value of guesses a,b,c,x {a}, {b}, {c},{x}")
        print(f"value of neg function at each place {negfunc(a):.3f},{negfunc(b):.3f},{negfunc(c):.3f},{negfunc(x):.3f} ")
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
    return x


if __name__ == "__main__":
    gs_guess=golden_section(-2,4,1e-2)
    print(f"{gs_guess}, value of func here is {func(gs_guess)}")
    paraguess=parabolic_interpolation(1.7,2,2.7,5)
    print(f"{paraguess}, value of func here is {func(paraguess)}")