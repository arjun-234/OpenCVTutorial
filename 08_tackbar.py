import cv2
import numpy as np

img = np.zeros((300,650,3),np.uint8)
cv2.namedWindow('image')

def nothing(x):
	print(x)

# arguments= tackbarname,
# windowname,
# initialvalue of your tarckbar, 
# maximumvalueoftrackbar, 
# callbackfunction
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

switch = '0/1'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
	cv2.imshow('image',img)
	k = cv2.waitKey(1)

	if k == 27:
		break

	b = cv2.getTrackbarPos('B', 'image')
	g = cv2.getTrackbarPos('G', 'image')
	r = cv2.getTrackbarPos('R', 'image')
	s = cv2.getTrackbarPos(switch, 'image')

	if s == 0:
		img[:] = 0
	else:
		img[:] = [b,g,r]

cv2.destroyAllWindows()