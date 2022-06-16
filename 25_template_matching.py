import cv2
import numpy as np

dog = cv2.imread("dog.jpg")
dog_grey = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
dog_eye = cv2.imread("dog_eye.jpg", 0)

w, h = dog_eye.shape[::-1]

res = cv2.matchTemplate(dog_grey, dog_eye, cv2.TM_CCORR_NORMED )

threshold = 0.99;
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(dog, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)

cv2.imshow("img", dog)
cv2.waitKey(0)
cv2.destroyAllWindows()