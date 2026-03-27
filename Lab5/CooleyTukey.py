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
def DividedDifference3(x0,y0,x1,y1,x2,y2):
    left=(y2-y1)/((x2-x1)*(x2-x0))
    right=(y1-y0)/((x1-x0)*(x2-x0))
    return left-right
def CubicSpline(xmatrix,ymatrix):
    #make D matrix
    d_matrix=np.zeros(shape=(len(xmatrix)+1,1))
    coefficient_matrix=2*np.identity(len(xmatrix))
    d_matrix[0]=6*DividedDifference3(xmatrix[0],ymatrix[0],xmatrix[0],ymatrix[0],xmatrix[1],ymatrix[1])
    coefficient_matrix[0][1]=1
    for k in range(1,len(xmatrix)):
        if k!=len(xmatrix):
            d_matrix[k]=6*DividedDifference3(xmatrix[k-1],ymatrix[k-1],xmatrix[k],ymatrix[k],xmatrix[k+1],ymatrix[k+1])
        hi=xmatrix[k+1]-xmatrix[k]
        hi1=xmatrix[k+2]-xmatrix[k+1]
        mui=hi/(hi+hi1)
        coefficient_matrix[k][k-1]=mui
        if k!=len(xmatrix):
            coefficient_matrix[k][k+1]=1-mui


    coefficients=np.linalg.solve(coefficient_matrix,d_matrix)
    return coefficients

if __name__=="__main__":
    testmatrix=np.array([0,1,2,3,4,5,6,7])
    print(np.fft.fft(testmatrix).shape)
    test=FFT2(testmatrix)
    print(test.shape)
    xmatrix=np.array([[1],[2]])
    print(xmatrix)
    ymatrix=np.array([[2],[3]])
    #coefficients=CubicSpline(xmatrix,ymatrix)
    