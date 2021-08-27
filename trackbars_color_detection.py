import cv2
import numpy as np
import pandas as pd
img=cv2.imread(r"E:\numpy\colorfull.jpg")
img=cv2.resize(img,(500,500))
blank=np.zeros((500,500,3)).astype(np.uint8)
def nothing(a):
       pass

cv2.namedWindow('colorbars')
cv2.createTrackbar('h1','colorbars',0,180,nothing)
cv2.createTrackbar('s1','colorbars',0,255,nothing)
cv2.createTrackbar('v1','colorbars',0,255,nothing)
cv2.createTrackbar('h2','colorbars',0,180,nothing)
cv2.createTrackbar('s2','colorbars',0,255,nothing)
cv2.createTrackbar('v2','colorbars',0,255,nothing)


while True:
    cv2.imshow('img',img)
    h1 = cv2.getTrackbarPos('h1','colorbars')
    s1 = cv2.getTrackbarPos('s1', 'colorbars')
    v1 = cv2.getTrackbarPos('v1', 'colorbars')
    h2 = cv2.getTrackbarPos('h2', 'colorbars')
    s2 = cv2.getTrackbarPos('s2', 'colorbars')
    v2 = cv2.getTrackbarPos('v2', 'colorbars')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_range=np.array([h1,s1,v1])
    upper_range = np.array([h2, s2, v2])
    thresh = cv2.inRange(hsv, lower_range, upper_range)
    bitwise=cv2.bitwise_and(img,img,mask=thresh)
    blank[:,:]=upper_range
    cv2.imshow('blank',cv2.cvtColor(blank,cv2.COLOR_HSV2BGR))
    cv2.imshow('hsv',hsv)
    cv2.imshow('and',bitwise)










    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
                mode = not mode
    elif k == 27:
                break
cv2.destroyAllWindows()
