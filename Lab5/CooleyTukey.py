import math
import numpy as np
import cmath
def FFT(sequence,stride=1):
    num_samples=len(sequence)
    final_answer=np.zeros(shape=(num_samples))
    if abs(math.log(len(sequence),2)-math.floor(math.log(len(sequence),2))) > 1e-9:
        raise ValueError("input sequence does not have length of power of 2")
    if num_samples==1:
        final_answer[0]=sequence
    else:
        fft(sequence[0::2]) # even indices
        fft(sequence[1::2])
        for k in range(0,(num_samples/2)-1):
            p=sequence(k)
            q=math.exp((-2*math.pi*1j/num_samples)*k)*sequence(k+num_samples/2)
            final_answer[k]=p+q
            final_answer[k+num_samples/2]=p-q
        
    

    def _recursiveFFT(Sequence):
        return 0
    
    #trying to just exactly match the wikipedia article
def FFT(sequence,num_samples,stride):
    if num_samples==1:
        return sequence # not sure how to get the right index in here
    else:
        #need to do some array slicing to make this work
        FFT(sequence[0::2],num_samples/2,2*stride)
        FFT(sequence[1::2],num_samples/2,2*stride)
        for k in range(0,(num_samples/2)): #the -1 is taken care of by the range function
            p=answer[k]
            q=math.exp(-2*math.pi*1j*k/num_samples)*answer[k+num_samples/2]
            answer[k]=p+q
            answer[k+num_samples/2]=p-q

#following code from the explainer video
def FFT2(sequence):
    N=len(sequence)
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
    