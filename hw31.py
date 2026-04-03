import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.polynomial.polynomial import Polynomial as p
def Vandermonde(array):
    num_pairs=len(array)
    y_matrix=np.zeros(shape=(num_pairs,1))
    matrix=np.identity(num_pairs)
    for row in range(0,num_pairs):
        y_matrix[row]=array[row][1]
        for index in range(0,num_pairs):
            matrix[row][index]=array[row][0]**index
    print(matrix)
    print(y_matrix)
    coefficients=np.linalg.solve(matrix,y_matrix)
    coefficients=coefficients.reshape(-1)
    return p(coefficients)
def Lagrange(array):
    Langrange_poly=p(0)
    print(array[0][1])
    for i in range(0,len(array)):
        running_polynomial=p(1)
        for j in range(0,len(array)):
            if j!=i:
                new_polynomial=p(((-array[j][0]/(array[i][0]-array[j][0])),1/(array[i][0]-array[j][0])))
                running_polynomial=running_polynomial*new_polynomial
        Langrange_poly+=(running_polynomial*array[i][1])
    print(Langrange_poly)
    return Langrange_poly
def make_points(num_points):
    x_values=np.linspace(0,2,num_points)
    f= lambda x: np.cos(2*math.pi*x)
    matrix=np.zeros(shape=(num_points,2))
    for x in range(0,num_points):
        matrix[x]=(x_values[x],f(x_values[x]))
    return matrix
def bisection(a,b,polynomial):
    done=False
    while not done:
        xm=(a+b)/2
        result=polynomial(xm)
        if abs(b-a)<1e-8:
            return xm
            done=True 
        else:
            if (polynomial(a))*(result) >0:
                a=xm
            else:
                b=xm
if __name__=="__main__":
    # test1=np.array([[300,.616],[400,.525],[500,.457]])
    # test2=np.arange(300,500,50)
    # test3=Vandermonde(test1)
    # print(test3)
    # fig=plt.plot(test2,test3(test2))
    # plt.show()
    # RI_table=np.array([[6563,1.50883],[6439, 1.50917],[5890, 1.51124],[5338, 1.51386],[5086, 1.51534],[4861, 1.51690],[4340, 1.52136],[3988, 1.52546]])
    # RI_interpolation=Lagrange(RI_table)
    test_x=np.arange(0,2,0.01)
    i=5
    while i <=100:
        test=make_points(i)
        n5=Vandermonde(test)
        fig=plt.plot(test[0:,0],n5(test))
        plt.show()
        i+=5
        