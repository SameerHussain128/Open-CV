# WEB CAMERA OPEN

import cv2
import numpy as np

# Doing some Face Recognition with the webcam
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #  canvas = detect(gray, frame)
  
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()