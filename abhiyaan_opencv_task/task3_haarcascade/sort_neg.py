import cv2
import os 


folder='/home/ankit/opencv_workspace/neg'
count=1
for filename in os.listdir(folder):
	img=cv2.imread(os.path.join(folder,filename),cv2.IMREAD_GRAYSCALE)
	cv2.imshow('img',img)
	resized_image=cv2.resize(img,(100,100))
	status=cv2.imwrite("neg"+str(count)+".jpg",resized_image)
	print(status)
	count=count+1

	cv2.waitKey()
	
	
	
	
	



