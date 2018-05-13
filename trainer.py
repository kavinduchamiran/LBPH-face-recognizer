import numpy as np
import cv2
from time import sleep


# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#check if eyes in face
cap = cv2.VideoCapture(1)

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (0,0)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

i = 0

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+256,y+256),(255,0,0),2)
        roi_gray = gray[y:y+256, x:x+256]
        roi_color = img[y:y+256, x:x+256]
                                
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27 or i == 20:
        break

    if k == ord('c'):
        i+=1
        crop_img = img[y: y + 256, x: x + 256] # Crop from x, y, w, h -> 100, 200, 300, 400
        cv2.imwrite("training/face" + str(i) + ".jpg", cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY))
            
            
cap.release()   
cv2.destroyAllWindows()
