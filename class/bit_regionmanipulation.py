# importing the  cv module
import cv2
# reading the image
img = cv2.imread('/home/abhilashaopgautam/opencv-n/cat.jpg')
# import numpy for the math
import numpy as np
# manipulating a single bit
img[55,55] = (0,0,255 )
# manipulating a particular region
img[9:50,5:50] = (255,0,0)
# displaying the image
cv2.imshow('cat it is ',img)
cv2.waitKey(0)

