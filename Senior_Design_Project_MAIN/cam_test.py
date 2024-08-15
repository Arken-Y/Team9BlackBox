import cv2

cam1 = cv2.VideoCapture(0)
frame_width1 = int(cam1.get(3))
frame_height1 = int(cam1.get(4))

frame_size1 = (frame_width1, frame_height1)
writer1 = cv2.VideoWriter('test1.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, frame_size1)
count = 0
while True:
	ret, image1 = cam1.read()
	#print('Camera Start')
	writer1.write(image1)
	count += 1
	if count == 1:
		print("camera start")
	cv2.imshow('Cam1', image1)
	
cam1.release()
writer1.release()
cv2.destroyAllWindows()
