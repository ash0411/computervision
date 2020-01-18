import cv2 as cv
import numpy as np
import imutils
from imutils import contours
card  = cv.imread('/home/ash/opencv_projects/images/card.jpg')
ocr = cv.imread('/home/ash/opencv_projects/images/ocr.png')
ocr = cv.cvtColor(ocr,cv.COLOR_BGR2GRAY)
thresh = cv.threshold(ocr,10,255,cv.THRESH_BINARY_INV)[1]
# cv.imshow('thresh',thresh)
# cv.waitKey(0)
# aspect ratio width/height
digits = {}
ocrcnts = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
ocrcnts = imutils.grab_contours(ocrcnts) 
ocrcnts = contours.sort_contours(ocrcnts,"left-to-right")[0]
for i,c in enumerate(ocrcnts):
    (x,y,w,h) = cv.boundingRect(c)
    roi = thresh[y:y+h,x:x+w]
    
    roi = cv.resize(roi,(50,80))
    digits[i] = roi
# for i in range(10):
#     cv.imshow(str(i),digits[i])
#     cv.waitKey(0)
#------------------------using gradients for card reading -------------------------------------------]
rectkernel = np.ones((3,9),dtype="uint8")
sqrkernel = np.ones((5,5),dtype="uint8")
card = imutils.resize(card,width=300)
gray = cv.cvtColor(card,cv.COLOR_BGR2GRAY)
tophat = cv.morphologyEx(gray,cv.MORPH_TOPHAT,sqrkernel)
gradX = cv.Sobel(tophat,cv.CV_32F,1,0,sqrkernel)
#print(gradX)
gradX = np.absolute(gradX)
#print("absolute value")
#print(gradX)
(minVal,maxVal) = (np.min(gradX),np.max(gradX))
# min and max gives values of min and max while argmin and argmax give values of the index
#print(minVal,maxVal)
gradX = ((gradX-minVal)/(maxVal-minVal))*255 # normalization
gradX = gradX.astype("uint8")

gradX = cv.morphologyEx(gradX,cv.MORPH_CLOSE,rectkernel)
thresh =  cv.threshold(gradX,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
# cv.imshow('thresh',thresh)
# cv.waitKey(0)
thresh = cv.morphologyEx(gradX,cv.MORPH_CLOSE,sqrkernel)
cnts = cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
locs = []
for (i,c) in enumerate(cnts):
    (x,y,w,h) = cv.boundingRect(c)
    ar = w/float(h)
    print(ar)
    if ar>2.5 and ar <4.0:
        #if (w>40 and w<55) and (h >10 and h<20):
        locs.append((x,y,w,h))
for (x,y,w,h) in locs:
    cv.rectangle(card,(x,y),(x+w,y+h),(0,0,255),1)
cv.imshow("image",card)
cv.waitKey(0)
