import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(255,0,0),-1)

        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(120,120,65),5)

        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        cv2.circle(img,(x,y),3,(255,0,0),-1)

        custom_clr_img = np.zeros((512,512,3) ,np.uint8)
        custom_clr_img[:] = [blue,green,red]

        cv2.imshow('color-tab',custom_clr_img)

img = cv2.imread('python.yudiz.png')
cv2.imshow('image', img)

points=[]

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
