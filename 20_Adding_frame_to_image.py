import cv2
import numpy as np

img1 = cv2.imread("frame.png") 
img = cv2.imread("dog.jpg") 
img1 = cv2.resize(img1,(500,500))
# cv2.imshow('frame',img)

dog = img[40:460, 25:470]
img1[40:460, 25:470] = dog

cv2.imshow('frame',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()