import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('back1.jpg')  # Load a color image (BGR)
img2 = cv.imread('newold.jpg', cv.IMREAD_GRAYSCALE)  # Load as grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert img to grayscale
plt.imshow(img)
plt.show()
new = cv.cvtColor(img2, cv.COLOR_GRAY2BGR)  # Convert grayscale img2 to BGR (still looks gray but has 3 channels)
#blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#edge cansade
canny=cv.Canny(img,125,175)
#dilatwe 
dilated=cv.dilate(canny,(3,3),iterations=1)
#resize
res=cv.resize(img,(400,400))
#crop
cropped=img[50:200,200:400]
#hsv color space
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
#lab color space
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
#bgr2rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
cv.imshow('lab', lab)
cv.imshow('croped', cropped)
cv.imshow('color', res)
cv.imshow('hsv', hsv)
cv.imshow('newold', dilated)
cv.imshow('Grayscale of back1', gray)
cv.imshow('Original newold (color)', new)
cv.imshow('Original', canny)
cv.imshow('blur',blur)  
cv.waitKey(0)
cv.destroyAllWindows()
