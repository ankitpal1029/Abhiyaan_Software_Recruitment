import cv2
import numpy as np
# basics :sentdex open cv tutorial
for i in range(1,4):
    img=cv2.imread(str(i)+".png")
    a=np.asarray(img)
    if a[int(a.shape[0]/3)-int(a.shape[0]/6)][int(a.shape[1]/2)][2] == 255:
        cv2.imshow("red",img)
        print("red")
    elif a[int(a.shape[0])-int(a.shape[0]/6)][int(a.shape[1]/2)][1] ==255:
        cv2.imshow("green",img)
        print("green")
    else:
        cv2.imshow("yellow",img)
        print("yellow")
    cv2.waitKey()
