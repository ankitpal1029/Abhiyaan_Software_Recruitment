import cv2
import numpy as np


traffic_cascade_g=cv2.CascadeClassifier("/home/ankit/opencv_workspace/data/cascade.xml")
traffic_cascade_y=cv2.CascadeClassifier("/home/ankit/opencv_workspace/datay/cascade.xml")
traffic_cascade_a=cv2.CascadeClassifier("/home/ankit/opencv_workspace/dataa/cascade.xml")

img=cv2.imread("test3.png",1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


traffic_g=traffic_cascade_g.detectMultiScale(gray)
traffic_y=traffic_cascade_y.detectMultiScale(gray)
traffic_a=traffic_cascade_a.detectMultiScale(gray)

for (x,y,w,h) in traffic_g:
	if y<=360:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	

for (x,y,w,h) in traffic_y:
	if y<=360:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	

for (x,y,w,h) in traffic_a:
	if y<=360:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)





cv2.imwrite("detect_signal.jpg",img)
cv2.waitKey()