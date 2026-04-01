import numpy
import matplotlib.plot as plt

def Vandermonde(array):
    num_pairs=len(array)
    y_matrix=np.zeros(shape=(num_pairs,1))
    matrix=np.identity(num_pairs)
    for i in range(0,num_pairs):
        