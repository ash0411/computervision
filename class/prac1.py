import face_recognition
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
aashish_image = face_recognition.load_image_file("/home/ash/opencv_projects/images/opencvframe_0.png") # to load the image
aashish_face = face_recognition.face_encodings(aashish_image)[0]
#print(aashish_face)
#print(len(aashish_face))
known_face_encodings =[
    aashish_face
]
known_face_names = [
    'aashish bora'
]
process_frame = True
while True:
    ret,frame = cap.read()
    frame_resize = cv.resize(frame,(0,0),fx=0.25,fy = 0.25)
    rgb_frame = cv.cvtColor(frame_resize,cv.COLOR_BGR2RGB)
    if process_frame:
        face_locations = face_recognition.face_locations(rgb_frame,model = 'cnn')
        face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)
        names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
            name = 'unknown'
            face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)
            best_match_index = np.argmin(face_distances)# returns the minimum value in the entire array to match which is the best index for the particular face
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            names.append(name)
    process_frame = not process_frame

    # for rectangle display
    for (top,right,bottom,left),name in zip(face_locations,names):
        top *=4
        right *=4
        bottom *=4
        left *=4
    # drawing a box
        cv.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
    # writing a name
        cv.putText(frame,name,(left +6,bottom -6),cv.FONT_HERSHEY_PLAIN,2,(0,0,255),1)
    cv.imshow('face recog',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
