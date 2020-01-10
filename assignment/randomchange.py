# assignment to paint a canvas in a set of random values
import cv2 as cv
from random import random
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("/home/ash/opencv_projects/images/goku.jpeg")
canvas = np.ones((300,300,3),dtype = "uint8")*255
print(img.shape[0],img.shape[1])
b,g,r = cv.split(img)
print(r.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j] = (b[i,j]*random(),g[i,j]*random(),r[i,j]*random())
#cv.imshow("canvas",canvas)
cv.imshow("goku",img)
cv.waitKey(0)