import cv2

img = cv2.imread("python.yudiz.png",0)

cv2.imshow("IMAGE-TAB",img)

k = cv2.waitKey(0) 

cv2.destroyAllWindows()

#save image
# cv2.imwrite("gray.python.yudiz.png",img)
# print("image has been saved successfully")

if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite("gray.python.yudiz.png",img)
	print("image has been saved successfully")
	cv2.destroyAllWindows()
