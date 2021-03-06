import cv2
import sys

mouthCascade = cv2.CascadeClassifier('mouth.xml')
#face_cascade = cv2.CascadeClassifier('mouth xml.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
faceCascade = cv2.CascadeClassifier('face.xml')
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mouth = mouthCascade.detectMultiScale(gray, 1.3, 5)
    face = faceCascade.detectMultiScale(gray, 1.3, 5)
    # Draw a rectangle around the faces
    for (x, y, w, h) in mouth:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
