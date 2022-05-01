import cv2
import numpy as np
   
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('part1.mp4')
   
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
count = 0
while(cap.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()
  
  if ret == True:
    
    # Display the resulting frame
    cv2.imshow('Frame', frame)
       
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

    if cv2.waitKey(25) & 0xFF == ord('c'):
      print(count)
      cv2.imwrite('Frame'+str(count)+'.jpg', frame)
      count += 1
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()



img = cv2.imread('Frame0.jpg')

template = cv2.imread('Frame1.jpg')
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 3)
# show the output image
cv2.imshow("Output", img)
cv2.waitKey(0)

cv2.imshow('template maching',result)

