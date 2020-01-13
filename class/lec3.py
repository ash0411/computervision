import numpy as np
import cv2 as cv
image = cv.imread('/home/ash/opencv_projects/images/goku.jpeg')
# thresholding 
'''
retval,threshold = cv.threshold(image,20,255,cv.THRESH_BINARY)
cv.imshow("threshold",threshold)
gray_scale = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
retval,threshold = cv.threshold(image,20,255,cv.THRESH_BINARY)
cv.imshow("gray threshold",gray_scale)
'''
'''
def thresholding(image,threshold_val,max_val = 255):
    #zeros = np.zeros((img.shape[0],img.shape[1]),dtype = "uint8")
    img = np.where(image < threshold_val ,0,255)
    img1 = np.uint8(img)
    print(img1)
    return img1
img = thresholding(image,20)
'''
'''
adaptiveThresholdImage = cv.adaptiveThreshold(gray_scale,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,105,1)# 1 is a constant that is subtracted from the mean
adaptiveThresholdImage1 = cv.adaptiveThreshold(gray_scale,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,105,1)# 1 is a constant that is subtracted from the mean
cv.imshow('adaptive',adaptiveThresholdImage)
cv.imshow('MEAN',adaptiveThresholdImage1)
#cv.imshow("img",img)
'''
# vedios
# capturing teh cideo from the primary cammera
cap = cv.VideoCapture(0)
# running the loop unless any key is pressed
while True:
    # returning the (b,g,r) and frame
    ret,frame = cap.read()
    #frames = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #flipped_image = cv.flip(frame,0)
    '''
    # for color screen
    zeros = np.zeros((frame.shape[0],frame.shape[1]),dtype = "uint8")
    b,g,r = cv.split(frame)
    red = cv.merge([zeros,zeros,r])
    orange = np.array([0,165,255],dtype=uint8)
    #orange = cv.merge([zeros,(g/255)*165,r])
    green = cv.merge([zeros,g,zeros])
    cv.imshow('red',red)
    cv.imshow('orange',orange)
    cv.imshow('green',green)
    '''
    cv.rectangle(frame,(254,6),(535,430),(0,255,0),1)
    cv.putText(frame,"Aashish Bora",(260,410),cv.FONT_HERSHEY_COMPLEX,1,(135,255,0),2)
    cv.imshow('frame',frame)
    # waiting for a key to be pressed 
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# releasing thee camera
cap.release()
    #destroting all windows
cv.destroyAllWindows()
#cv.imshow("image",image)
cv.waitKey(20000)