import cv2
import numpy as np

img = cv2.imread('img/menu.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)


minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(thresh,1,np.pi/180,15,minLineLength,maxLineGap)

for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(thresh,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('hough',thresh)


cv2.waitKey(0)
cv2.destroyAllWindows
