import os
import numpy as np
import cv2 as cv
people=['ben_affleck','chris evans','bale','bradpitt']
p=[]
dir=r"C:\Users\acer\OneDrive\Documents\faces"
features=[]
labels=[]
haar_cascade=cv.CascadeClassifier('computervision\haar_face.xml')
def create_train():
    for person in people:
        path=os.path.join(dir,person)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            face=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
            for (x,y,w,h) in face:
               faces_roi=gray[y:y+h,x:x+w]
               features.append(faces_roi)
               labels.append(label)
create_train()
print(f'length of features: {len(features)}')
print(f'length of labels: {len(labels)}') 
print('training done') 
features=np.array(features,dtype='object')    
labels=np.array(labels)           
face_recog=cv.face.LBPHFaceRecognizer_create()
face_recog.train(features,labels)
face_recog.save('face_celeb.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)