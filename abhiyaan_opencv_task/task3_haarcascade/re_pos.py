import cv2
import os 

folder='/home/ankit/opencv_workspace/images'
img=cv2.imread(os.path.join(folder,'traffic_a.png'))
resized_image=cv2.resize(img,(20,50))
status=cv2.imwrite("traffic.jpg",resized_image)
print(status)
