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
	c0=(18-30**0.5)/36
	c1=(18+30**0.5)/36
	c2=c1
	c3=c0
	x0=-(((525+70*(30**0.5))**.5)/35)
	x1=-(((525-70*(30**0.5))**.5)/35)
	x2=-1*x1
	x3=-1*x0

if __name__=="__main__":
	func=lambda x: np.exp(-3*x)*np.sin(4*x)
	answer=Composite_Trapezoid(func,10,0,3.7)
	print(f"Composite trapezoid of func = {answer}")