import cv2 as cv
import numpy as np
image = cv.imread('/home/ash/opencv_projects/images/book.jpeg')
# color filtering
# cap = cv.VideoCapture(0)
# while True:
#     ret,frame = cap.read()
#     hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
#     lower_red = np.array([10,130,140])# 5,230,230 for blue  the values inside is for green 40,100,100
#     upper_red = np.array([220,255,255])# basically we give range in bgr and detect the color in that particular range 220,255,255 80,255,255
    
#     mask = cv.inRange(hsv,lower_red,upper_red)
#     res = cv.bitwise_and(frame,frame,mask = mask )# to perform bitwise end between 2 identical frames which will result in the same page and masking it between lower_red and upper_end
    
#     kernel = np.ones([10,10],np.uint8)/100
#     smoothed = cv.filter2D(res,-1,kernel)
    
#     median_blur = cv.medianBlur(res,15)
#     gaussian_blur = cv.GaussianBlur(res,(15,15),0)
    # # erosion
    # erosion = cv.erode(mask,kernel,iterations=1) 
    # dilation = cv.dilate(mask,kernel,iterations=1)
    # opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
    # closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
    # cv.imshow('opening',opening)
    # cv.imshow('closing',closing)
    #cv.imshow('erosion',erosion)
    #cv.imshow('dilation1',dilation)
    # cv.imshow("gaussian blur",gaussian_blur)
    # cv.imshow('median_blur',median_blur)
    # cv.imshow('smooth',smoothed)
    # cv.imshow('res',res)
    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     break
cv.circle(image,(122,5),1,(255,0,0),3)
cv.circle(image,(253,31),1,(255,1,1),3)
cv.circle(image,(4,88),1,(255,0,0),3)
cv.circle(image,(152,192),1,(255,0,0),3)
points1 = np.float32([[4,88],[152,192],[122,5],[253,31]])
points2 = np.float32([[0,0],[253,0],[0,192],[253,192]])
m = cv.getPerspectiveTransform(points1,points2)
transformed_image = cv.warpPerspective(image,m,(253,192))
cv.imshow("transformed image",transformed_image)
cv.imshow("goku",image)
cv.waitKey(0)
