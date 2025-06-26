import cv2 as cv
import numpy as np
img=cv.imread('back1.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8')
def resize(frame,scale=0.25):
    #for images video live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
circle = cv.circle(blank, (700,700) , 100, 255, -1)
masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('circle',resize(circle))
cv.imshow('masked',resize(masked))
cv.waitKey(0)