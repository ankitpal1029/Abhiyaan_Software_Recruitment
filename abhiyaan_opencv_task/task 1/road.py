import cv2
import numpy as np

img = cv2.imread('a.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
Lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
def distance(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

for i in range(Lines.shape[0]):
    for x1,y1,x2,y2 in Lines[i]:
        if distance(x1,y1,x2,y2)> 800:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

        

cv2.imwrite('houghlines5.jpg',img)