import cv2 as cv
img =cv.VideoCapture(0)

def resize(frame,scale=0.75):
    #for images video live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
def changeRes(width,height):#for live video
    img.set(3,width)
    img.set(4,height)
while True:
    isTrue,frame=img.read()
    frame=resize(frame,0.5)
    cv.imshow('dev',frame)
    if cv.waitKey(20) & 0xff==ord('d'):
        break
img.release()

cv.destroyAllWindows()