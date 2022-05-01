import numpy as np
import cv2
import matplotlib.pyplot as plt

bg = cv2.imread('Frame0.jpg')
bg = cv2.cvtColor(bg,cv2.COLOR_BGR2RGB)

plt.imshow(bg)

face = cv2.imread('frame.png')
face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)

plt.imshow(face)

height, width, channels = face.shape

methods = ['cv2.TM_CCORR_NORMED',     'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for x in methods:
    bg_copy = bg.copy()
    method = eval(x)
    result = cv2.matchTemplate(bg_copy,face,method)

    min_va, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0]+width,top_left[1]+height)

    cv2.rectangle(bg_copy,top_left,bottom_right, 255, 10)

    plt.subplot(121)
    plt.imshow(result)
    plt.title('Result of Template Matching')

    plt.subplot(122)
    plt.imshow(bg_copy)
    plt.title('Match Point')
    plt.suptitle(x)
    plt.show()
