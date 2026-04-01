import math
import numpy as np
import cmath

#following code from the explainer video
def FFT2(sequence):
    N=len(sequence)
    if not( (N & (N-1) == 0) and N != 0):
        raise ValueError("number is not a power of 2")
    if N==1:
        return sequence
    omega=cmath.exp(-2*math.pi*1j/N)
    even,odd=sequence[0::2],sequence[1::2]
    y_even,y_odd=FFT2(even),FFT2(odd)
    y_current=np.zeros(shape=(N,),dtype='complex')
    for j in range(0,N//2):
        y_current[j]=y_even[j]+(omega**j)*y_odd[j]
        y_current[j+N//2]=y_even[j]-(omega**j)*y_odd[j]
    return y_current

def DD1(x1,x0,y1,y0):
    return (y1-y0)/(x1-x0)

def CubicSpline(xmatrix,ymatrix):
    #This is using the process detailed in the book for the natural boundary condition
    result=np.zeros(shape=(len(xmatrix),))
    h_values=np.zeros(shape=(len(xmatrix)-1,))
    b_matrix=np.zeros(shape=(len(xmatrix)-1,))
    d_matrix=np.zeros(shape=(len(xmatrix)-1,))
    coefficient_matrix=np.identity(len(xmatrix))
    #set up result matrix
    for k in range(1,len(result)-1):
        result[k]=3*(DD1(xmatrix[k+1],xmatrix[k],ymatrix[k+1],ymatrix[k])-DD1(xmatrix[k],xmatrix[k-1],ymatrix[k],ymatrix[k-1]))
    #set up equation matrix
    for i in range(1,len(coefficient_matrix)-1):
        h_i=xmatrix[i]-xmatrix[i-1]
        h_i_plus_1=xmatrix[i+1]-xmatrix[i]
        h_values[i-1]=h_i
        h_values[i]=h_i_plus_1
        coefficient_matrix[i][i-1]=h_i
        coefficient_matrix[i][i]=2*(h_i+h_i_plus_1)
        coefficient_matrix[i][i+1]=h_i_plus_1

    coefficients=np.linalg.solve(coefficient_matrix,result)
    #solve for d values and b values
    for i in range(0,len(d_matrix)):
        d_matrix[i]=(coefficients[i+1]-coefficients[i])/h_values[i]
        b_matrix[i]=((ymatrix[i+1]-ymatrix[i])/h_values[i])-(h_values[i]/3)*(2*coefficients[i]+coefficients[i+1])
    spline_matrix=np.concatenate((ymatrix[0:-1],b_matrix,coefficients[0:-1],d_matrix)).reshape((-1,4),order='F')
    return spline_matrix
def interpolate(coefficient_matrix,x,x_matrix,matrix_spacing):
    values=np.zeros(shape=(len(x),))
    for x0 in range(0,len(x)):
        row=int(x[x0]//(matrix_spacing))
        if row>=len(coefficient_matrix):
            row=len(coefficient_matrix)-1
        #calc interpolation function for the given point
        values[x0]= coefficient_matrix[row][0]+coefficient_matrix[row][1]*(x[x0]-x_matrix[row])+coefficient_matrix[row][2]*((x[x0]-x_matrix[row])**2)+coefficient_matrix[row][3]*((x[x0]-x_matrix[row])**3)
    return values
if __name__=="__main__":
    xmatrix=np.array([[3],[4.5],[7.0],[9.0]])
    ymatrix=np.array([[2.5],[1],[2.5],[0.5]])
    coefficients=CubicSpline(xmatrix,ymatrix)
    print(coefficients)
    