import cv2
from tracker import *
#from itertools import izip_longest

cap = cv2.VideoCapture(r"C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\4 - March\29th\object_tracking\highway.mp4")

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

