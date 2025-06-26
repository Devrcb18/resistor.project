import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('computervision\idrive.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('new',gray)
circle = cv.circle(blank, (690,490) , 350, 255, -1)
masked=cv.bitwise_and(img,img,mask=circle)
gray_hist=cv.calcHist([masked],[0],None,[256],[0,256])
#color histogram
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
cv.imshow('circle',circle)
cv.imshow('masked',masked)
plt.show()
cv.waitKey(0)