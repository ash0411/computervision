import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('"/home/ash/opencv_projects/images/goku.jpeg')
#img_gray = cv.imread('cat.jpeg',0)
'''
#CONVERTING TO GRAY SCALE
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('cat grey',img_gray)
'''
'''#HSV COLOR
hsv_image = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("h",hsv_image[:,:,0])
cv.imshow("s",hsv_image[:,:,1])
cv.imshow("v",hsv_image[:,:,2])
'''
"""
#splitting into blue green and red
zeros = np.zeros((img.shape[0],img.shape[1]),dtype = "uint8")
b,g,r = cv.split(img)
red = cv.merge([zeros,zeros,r])
blue = cv.merge([b,zeros,zeros])
green = cv.merge([zeros,g,zeros])
cv.imshow("red",red)
cv.imshow("blue",blue)
cv.imshow("green",green)
"""
"""
#histograms(only running in jupyter)
hist = cv.calcHist([img],[0],None,[256],[0,256])
cv.calcHist()
cv.imshow('hist',hist)
"""
"""
#pixel maniputlation
(b,g,r) = img[0,0]
img[164:185,73:210] = (255,255,255)
cv.imshow('image',img)
"""
"""
# region manipulation
corner = img[0:200,0:800]
cv.imshow('image',corner)
"""
#drawing

canvas = np.ones((300,300,3),dtype = "uint8")*255
'''
cv.line(canvas,(0,0),(300,300),(0,255,0),3)
#cv.rectangle(canvas,(0,0),(60,60),(255,0,0),2)
cv.rectangle(canvas,(0,0),(60,60),(255,0,0),-1)# it fills the rectangle
#cv.circle(canvas,(240,40),10,(255,0,0),2)
#cocentric circles
for i in range(1,10):
    cv.circle(canvas,(150,150),10*i,(0,255,0),2)
cv.imshow("canvas",canvas)
'''
#PUTTING TEXT

#cv.putText(canvas,"I am a human",(0,150),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

# FLAG
cv.rectangle(canvas,(0,0),(300,100),(0,0,255),-1)
cv.rectangle(canvas,(0,100),(300,200),(255,255,255),-1)
cv.rectangle(canvas,(0,200),(300,300),(0,255,0),-1)
cv.circle(canvas,(150,150),50,(255,0,0),1)

cv.imshow("canvas",canvas)
#LECTURE 3

#cv.imshow('cat',img)
cv.waitKey(0)