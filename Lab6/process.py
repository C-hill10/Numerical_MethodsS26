import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
import preprocessing
def gradient_vector(array):
    # 3d array, 2 entries for each pixel, x and y component of the vector there
    new_array=np.array(shape=(array.shape[0],array.shape[1],2))
    for row in range(0,array.shape[0]):
        for index in range(0,array.shape[1]):
            try:
                above=array[row-1][index]
            except IndexError:
                above=0
            try:
                below=array[row+1][index]
            except IndexError:
                below=0
            try:
                left=array[row][index-1]
            except IndexError:
                left=0
            try:
                right=array[row][index+1]
            except IndexError:
                right=0
            new_array[row][index][0]=(right-left)/2
            new_array[row][index][1]=(above-below)/2
    return new_array


def check_threshold(threshold,array):
    #i will be using the euclidian norm for this
    outlines=np.array(shape=(array.shape[0],array.shape[1]),dtype="boolean")
    for row in range(0,array.shape[0]):
        for index in range(0,array.shape[1]):
            if math.sqrt(array[row][index][0]**2+array[row][index][1]**2) >= threshold:
                outlines[row][index]=True
            else:
                outlines[row][index]=False

