import cv2 as cv
img=cv.VideoCapture(0)
haar_cascade=cv.CascadeClassifier('computervision\haar_face.xml')

while True:
    isTrue,frame=img.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for (x,y,w,h) in face:
       cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
       cv.imshow('dev',frame)
       cv.imshow('dev',gray)
    if cv.waitKey(20) & 0xff==ord('d'):
        break
     
img.release()

cv.destroyAllWindows()
haar_cascade=cv.CascadeClassifier('computervision\haar_face.xml')
