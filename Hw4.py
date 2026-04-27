import math
import matplotlib.pyplot as plt
import numpy as np


def TrapezoidalIntegration(a,b,fa,fb):
    return (0.5)*(fb+fa)*(b-a)

def ListTI(matrix):
    final_result=0
    for row in range(0,matrix.shape[0]-1):
        final_result+=TrapezoidalIntegration(matrix[row][0],matrix[row+1][0],
        matrix[row][1],matrix[row+1][1])
    return final_result

def Composite_Trapezoid(func,N,Lower_bound,Upper_bound):
    matrix=np.linspace(Lower_bound,Upper_bound,N)
    print(matrix)
    final_result=0
    for row in range(0,len(matrix)-1):
        final_result+=TrapezoidalIntegration(matrix[row],matrix[row+1],
        func(matrix[row]),func(matrix[row+1]))
    return final_result
def Gaussian_Quadrature_4Point(a,b,func):
	bound=lambda x:((b+a)+(b-a)*x)/2
	c0=(18-(30**0.5))/36
	c1=(18+(30**0.5))/36
	c2=c1
	c3=c0
	x0=-(((525+70*(30**0.5))**.5)/35)
	x1=-(((525-70*(30**0.5))**.5)/35)
	x2=-1*x1
	x3=-1*x0
	return .5*(b-a)*(c0*func(bound(x0))+c1*func(bound(x1))+c2*func(bound(x2))+c3*func(bound(x3)))
def composite_gaussian(a,b,func,N):
    matrix=np.linspace(a,b,N)
    final_result=0
    for row in range(0,len(matrix)-1):
        final_result+=Gaussian_Quadrature_4Point(matrix[row],matrix[row+1],
        func)
    return final_result
def adaptive_quadrature(a,b,func,tolerance):
	c=(a+b)/2
	d=(a+c)/2
	e=(c+b)/2
	h1=b-a
	h2=h1/2
	fa=func(a)
	fb=func(b)
	fc=func(c)
	fd=func(d)
	fe=func(e)
	I1=(h1/6)*(fa+4*fc+fb)
	I2=(h2/6)*(fa+4*fd+2*fc+4*fe+fb)
	Error=(I2-I1)/15
	if abs(Error) < tolerance:
		return I2+Error
	else:
		return (adaptive_quadrature(a,c,func,tolerance/2)
		+adaptive_quadrature(c,b,func,tolerance/2))
def Five_point_derivative(func,h):
	return lambda x:(1/(12*h))*(func(x-2*h)-8*func(x-h)+8*func(x+h)-func(x+2*h))
def second_derivative(func,h):
	First_derivative=Five_point_derivative(func,h)
	return Five_point_derivative(First_derivative,h)
def golden_section(func,a,b,epsilon):
    phi = (math.sqrt(5)+1)/2
    while abs(a-b)>epsilon:
        x1=b-(b-a)/phi
        x2=a+(b-a)/phi
        if func(x1)<func(x2):
            a=x1
        else:
            b=x2
    return (a+b)/2   
if __name__=="__main__":
	x_values=np.arange(0,450,5)
	func=lambda x: -156-(1/8)*np.exp(x-447)+78*(np.exp(-x/500)+np.exp(x/500))
	acceleration=second_derivative(func,1/16)
	solution=golden_section(acceleration,0,450,10e-6)
	print(f"The max acceleration is at {solution}, the value is {acceleration(solution)}")
	