import cv2 as cv
import numpy as np
img=cv.imread('pexels-tutsii-68590.jpg')
cv.imshow('boston',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
b,g,r=cv.split(img)
blue=cv.merge([b,blank,blank])
cv.imshow('blue',blue)
cv.imshow('red',r)
cv.imshow('green',g)
cv.waitKey(0)