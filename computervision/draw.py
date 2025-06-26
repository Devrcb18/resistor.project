import cv2 as cv
import numpy as np

img=cv.VideoCapture(0)
blank=np.zeros((500,500,3),dtype="uint8")#dummy
#painting the pixel
blank[20:30,30:40]=0,255,0#green 

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=3)
cv.circle(blank, (250,250),(50),(0,0,255),thickness=-1)
cv.line(blank,(250,250),(300,250),(255,0,0),thickness=4)
cv.putText(blank,'Origin',(250,250),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,34,40),1)
cv.imshow('1',blank)

# while True:
#     isTrue,frame=img.read()
#     cv.imshow('devansh',frame)
#     if cv.waitKey(20) & 0xff==ord('d'):
#         break
# img.release()

# cv.destroyAllWindows()
cv.waitKey(0)