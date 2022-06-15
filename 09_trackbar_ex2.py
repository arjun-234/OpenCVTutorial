import cv2
import numpy as np

# img = np.zeros((300,650,3),np.uint8)
 
cv2.namedWindow('image')

def nothing(x):
	print(x)

# arguments= tackbarname,
# windowname,
# initialvalue of your tarckbar, 
# maximumvalueoftrackbar, 
# callbackfunction

switch = '0/1(grayscale/color)'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
	img = cv2.imread("dog.jpg",1)
	
	k = cv2.waitKey(1)

	if k == 27:
		break

	s = cv2.getTrackbarPos(switch, 'image')
	if s == 0:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 
	else:
		# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		pass

	cv2.imshow('image',img)

cv2.destroyAllWindows()