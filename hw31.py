import numpy as np
import matplotlib.pyplot as plt

def Vandermonde(array):
    num_pairs=len(array)
    y_matrix=np.zeros(shape=(num_pairs,1))
    matrix=np.identity(num_pairs)
    for row in range(0,num_pairs):
        y_matrix[row]=array[row][1]
        for index in range(0,num_pairs):
            matrix[row][index]=array[row][0]**index
    coefficients=np.linalg.solve(matrix,y_matrix)
    coefficients=coefficients.reshape(-1)
    return np.polynomial.polynomial.Polynomial(coefficients[::-1])


if __name__=="__main__":
    myarray=np.array([(300,0.616),(400,.525),(500,.457)])
    polynomial=Vandermonde(myarray)
    print(polynomial)
    
        