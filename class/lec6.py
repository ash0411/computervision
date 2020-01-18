import cv2 as cv
import numpy as np
import face_recognition
# face and eye detection
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
cap = cv.VideoCapture(0)
while True:
    _,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5,5)
    eyes = eye_cascade.detectMultiScale(gray,1.5,5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h), (0, 0, 255), 2)
    for (x,y,w,h) in eyes:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


# cv.imshow('image',image)
# cv.waitKey(0)
