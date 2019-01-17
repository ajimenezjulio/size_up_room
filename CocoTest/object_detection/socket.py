import numpy as np
import cv2 as cv2

face_cascade = cv2.CascadeClassifier('/Users/juliocesar/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/Users/juliocesar/anaconda3/share/OpenCV/haarcascades/haarcascade_smileww.xml')

imgs = ['test_images/face.jpg', 'test_images/image1.jpg', 'test_images/image2.jpg', 'test_images/image3.jpg']

for img in imgs:
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
        cv2.rectangle(gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()