import cv2 as cv
import numpy as np
# template matching
image = cv.imread('/home/ash/opencv_projects/images/wheres_waldo.jpg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
template = cv.imread('/home/ash/opencv_projects/images/color_waldo_template.jpg',0)
res = cv.matchTemplate(gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
w,h = template.shape[::-1]# reversing it by [::-1]
loc = np.where(res >= threshold)
for x,y in zip(*loc[::-1]):
    cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
cv.imshow('image',image)
cv.waitKey(0)
