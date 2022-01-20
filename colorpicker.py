# This is colorpicker made by Arun Kumar

import cv2
import numpy as np


def nothing (x):
    print(x)

img = np.zeros([300,512,3],np.uint8)
   
cv2.namedWindow("color attechment")
s= "0:OFF\n1:ON"
cv2.createTrackbar(s, "color attechment", 0,1,nothing)
# Create trackbar
cv2.createTrackbar('R', 'color attechment', 0, 255, nothing)
cv2.createTrackbar('G', 'color attechment', 0, 255, nothing)
cv2.createTrackbar('B', 'color attechment', 0, 255, nothing)




while (1):
    cv2.imshow("color attechment",img)
    k=cv2.waitKey(1) &0xFF
    if k==ord('q'):
        break
    s1 = cv2.getTrackbarPos(s, "color attechment")
    r = cv2.getTrackbarPos('R', 'color attechment')
    g = cv2.getTrackbarPos('G', 'color attechment')
     
    b = cv2.getTrackbarPos('B', 'color attechment')
    
    if s1==0:
        img[:]= 0
    else:
        
        img[:]=[r,g,b]
     
     
cv2.destroyAllWindows()