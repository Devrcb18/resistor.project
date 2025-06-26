import numpy as np
import cv2 as cv

# Load classifier and recognizer
haar_cascade = cv.CascadeClassifier('computervision/haar_face.xml')
people = ['ben_affleck', 'chris evans', 'bale', 'bradpitt']

# Initialize recognizer
face_recog = cv.face.LBPHFaceRecognizer_create()
face_recog.read('face_celeb.yml')

# Load test image
img_path = r'C:\python\computervision\bale\b6.jpg'
img = cv.imread(img_path)
if img is None:
    print(f"Error: Could not read image at {img_path}")
    exit()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
if len(face_rect) == 0:
    print("No faces detected!")
    exit()

for (x, y, w, h) in face_rect:
    # Extract and resize face ROI
    face_roi = gray[y:y+h, x:x+w]
    face_roi = cv.resize(face_roi, (100, 100)) 
    label, confidence = face_recog.predict(face_roi)
    
    
    print(f'Person: {people[label]} (Confidence: {confidence:.2f})')
    
    # Draw rectangle and text
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    text = f"{people[label]} ({confidence:.2f})"
    cv.putText(img, text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# Show result
cv.imshow('Face Recognition', img)
cv.waitKey(0)
cv.destroyAllWindows()