import cv2 
import numpy as np
import time

cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

	diff = cv2.absdiff(frame1,frame2)
	gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

	blur = cv2.GaussianBlur(gray,(5,5),0)

	_,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

	dilated = cv2.dilate(thresh,None, iterations=3)
	contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# cv2.drawContours(frame1, contours, -1, (255,255,255), 1)
	for cont in contours:
		(x, y, w, h) = cv2.boundingRect(cont)
		print(x, y, w, h)
		if cv2.contourArea(cont) < 500:
			continue
		cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 255, 255), 1)
		cv2.putText(frame1, "Movement", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


	cv2.imshow("feed",frame1)
	cv2.imshow("diff",diff)
	cv2.imshow("blur",blur)
	cv2.imshow("thresh",thresh)
	time.sleep(0.1)

	frame1 = frame2
	ret, frame2 = cap.read()

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
cap.release()