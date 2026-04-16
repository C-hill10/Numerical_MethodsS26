import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
import preprocessing
from matplotlib.widgets import Slider
def gradient_vector(array):
    # 3d array, 2 entries for each pixel, x and y component of the vector there
    new_array=np.zeros(shape=(array.shape[0],array.shape[1],2))
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
def improved_gradient(array):
	# 3d array, 2 entries for each pixel, x and y component of the vector there
	new_array=np.zeros(shape=(array.shape[0],array.shape[1],2))
	for row in range(0,array.shape[0]):
		for index in range(0,array.shape[1]):
			try:
				above=array[row-1][index]
			except IndexError:
				above=0
			try:
				two_up=array[row-2][index]
			except IndexError:
				two_up=0
			try:
				two_left=array[row][index-2]
			except IndexError:
				two_left=0
			try:
				two_right=array[row+2][index]
			except IndexError:
				two_right=0
			try:
				two_down=array[row+2][index]
			except IndexError:
				two_down=0
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
			# for this one i'm using the centered difference formula in the textbook
			# the one with O(h^4) Error
			new_array[row][index][0]=(8*(right-left)+(two_right-two_left))/12
			new_array[row][index][1]=(8*(above-below)+(two_up-two_down))/12
	return new_array

def check_threshold(array,threshold=25):
    #i will be using the euclidian norm for this
    outlines=np.zeros(shape=(array.shape[0],array.shape[1]),dtype=int)
    for row in range(0,array.shape[0]):
        for index in range(0,array.shape[1]):
            if math.sqrt(array[row][index][0]**2+array[row][index][1]**2) >= threshold:
                outlines[row][index]=0
            else:
                outlines[row][index]=1
    return outlines
def mask(picture,threshold_array):
    modified_picture=np.zeros(shape=(picture.shape),dtype=int)
    for row in range(0,picture.shape[0]):
        for index in range(0,picture.shape[1]):
            for channel in range(0,picture.shape[2]):
                modified_picture[row][index][channel]=picture[row][index][channel]*threshold_array[row][index]
    return modified_picture

if __name__=="__main__":
	filename=input("please give the file name you would like to process:")
	done=False
	while not done:
		try:
			filename="images/"+filename+".jpg"
			print(filename)
			processed_image=preprocessing.read_image(filename)
			done=True
		except FileNotFoundError:
			print("please try again, file not found")
			filename=input("please give the file name you would like to process:")
	grey_image=preprocessing.preprocess(filename)
	gradient_vector=improved_gradient(grey_image)
	lines=check_threshold(gradient_vector)
	modified_picture=mask(processed_image,lines)
	fig,ax=plt.subplots()
	image=ax.imshow(modified_picture)
	axthreshold = fig.add_axes([0.25, 0.05, 0.65, 0.03])
	thresh_slider = Slider(
		ax=axthreshold,
		label='threshold',
		valmin=1,
		valmax=50,
		valinit=25,
	)
	def update(val):
		new_picture=mask(processed_image,check_threshold(gradient_vector,val))
		image.set_data(new_picture)
		fig.canvas.draw()
	thresh_slider.on_changed(update)
	ax.axis('off')
	plt.show() 

