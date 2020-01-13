import cv2 as cv
cam = cv.VideoCapture(0)
cv.namedWindow("test")
img_count = 0
while True:
    ret,frame = cam.read()
    cv.imshow("test",frame)
    if not ret:
        break
    k = cv.waitKey(1)
    if k%256 == 27:
        print("escape")
        break
    elif k%256 == 32:
        img_name = "opencvframe_{}.png".format(img_count)
        cv.imwrite("/home/ash/opencv_projects/images/"+img_name,frame)
        img_count = img_count + 1
cam.release()
cv.destroyAllWindows()    
cv.imwrite()