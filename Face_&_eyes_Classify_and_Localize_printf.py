import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\4 - March\24th\Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\4 - March\24th\Haarcascades/haarcascade_eye.xml')
 
img = cv2.imread(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\4 - March\24th\Computer-Vision-Tutorial-master\fruit\sam.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# Iterate over detected faces

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,255),2)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)
        
        name = input("Please enter your name: ")
        # Display the entered name on the image
        cv2.putText(img, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
cv2.destroyAllWindows()