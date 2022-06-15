import cv2

img = cv2.imread("dog.jpg",1)

# arguments=(image,x_cordinate,cordinate,line color(b,g,r),thickness of line)
img = cv2.line(img,(0,0),(255,255),(0,100,20), 2) #line
img = cv2.arrowedLine(img,(0,200),(200,250),(0,255,0), 2) #arraow
img = cv2.rectangle(img,(200,10),(250,200),(0,255,0), 2) #rectangle

# arguments=(image,center,radious,line color(b,g,r),thickness of line)
img = cv2.circle(img,(350,200),50,(0,255,0), 2) #circle

# write font on images
font = cv2.FONT_HERSHEY_SIMPLEX
#argument = image, text what you want to write, cordinate, font style, font size, colorr, line thickness, line type(optional)
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 4, cv2.LINE_AA)

cv2.imshow("DOG",img)
cv2.waitKey(0) 

cv2.destroyAllWindows()
