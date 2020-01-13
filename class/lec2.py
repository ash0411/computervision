import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
image = cv.imread('/home/ash/opencv_projects/images/goku.jpeg')
# here we are shifting the x and y axis by 1/4 the size of image
'''m = np.float32([[1,0,image.shape[0]//4],[0,1,image.shape[1]//4]])
translated_image = cv.warpAffine(image,m,(image.shape[0],image.shape[1]))
cv.imshow('translated image',translated_image)
# read truncation operation
# you can also see sentosa.io
'''

#rotation of image
# doubt in transpose of a matrix
'''
height,width = image.shape[:2]
print(height,width)
rotation_matrix = cv.getRotationMatrix2D((height//2,width//2),90,.9)
rotated_image = cv.warpAffine(image,rotation_matrix,(height,width))
cv.imshow("rotated image",rotated_image)
rotated_image2 = cv.transpose(image)
cv.imshow('transposed image',rotated_image2)
'''
# flipping an image

flipped_image = cv.flip(image,1)
ver_image = cv.flip(image,0)
both_flipped = cv.flip(image,-1)
cv.imshow("flipped_image",flipped_image)# horizontal flip
cv.imshow("ver_image",ver_image)# vertical flip
cv.imshow("both_flipped",both_flipped)# both horizontal and vertical flip

# scaling resizing and interpolation
'''
image_scaled = cv.resize(image,None,fx=0.20,fy=0.20)
print(image_scaled.shape)
cv.imshow("image_scaled",image_scaled)
'''
#image pyramids
# they help in image scaling in object detection










## Sharpening
"""
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])
sharped_image = cv.filter2D(image, -1, kernel_sharpening)
cv.imshow('sharped_image', sharped_image)

kernel_3x3 = np.ones((3, 3), np.float32)/9

## We use .filter2D to convolve the kernel with an image
## -1 means anchor is at kernel center
blurred = cv.filter2D(image, -1, kernel_3x3)
cv.imshow('blurred', blurred)

kernel_7x7 = np.ones((7, 7), np.float32)/9
# blurred_2 = cv.filter2D(image, -1, kernel_7x7
"""
cv.imshow("image",image)
cv.waitKey(30000)