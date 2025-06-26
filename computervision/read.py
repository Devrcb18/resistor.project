import cv2 as cv
img =cv.VideoCapture(0)

while True:
    isTrue,frame=img.read()
    cv.imshow('dev',frame)
    if cv.waitKey(20) & 0xff==ord('d'):
        break
img.release()

cv.destroyAllWindows()