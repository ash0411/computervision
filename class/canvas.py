#making of a canvas 
# importing the  cv module
import cv2
# makin
# import numpy for the math
import numpy as np
canvas = np.ones((300,300,3),dtype= 'uint8')*255
canvas2 = np.ones((300,300,3),dtype= 'uint8')*255
green = (0,255,0)
red = (0,0,255)
blue = ( 255,0,0)
blank = (255,255,255)
#canvas2 = np.ones((300,300,3),dtype= 'uint8')*255
#cv2.rectangle(canvas,(0,300),(300,100),red,-1)
#cv2.line(canvas,(0,300),(300,0),red,5)
cv2.rectangle(canvas,(0,0),(300,100),red,-1)
cv2.rectangle(canvas,(0,100),(300,200),blank,-1)
cv2.rectangle(canvas,(0,200),(300,300),green,-1)
cv2.circle(canvas,(150,150),50,blue,2)
for i in range(0,200,15):
	cv2.circle(canvas2,(150,150),i,green,2)
cv2.imshow('canvas2 ',canvas2)
cv2.imshow('canvas ',canvas)
#cv2.imwrite('canvas.jpg',canvas)
cv2.waitKey(0)
