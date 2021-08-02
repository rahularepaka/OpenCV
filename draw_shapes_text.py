import cv2
import numpy as np

img = cv2.imread("Photos\\arduino.jpg")

blank = np.zeros((500,500,3),dtype='uint8')

#fill in certain colour
blank[200:300,300:400] = 0,0,255
#cv2.imshow("Green",blank)

#Draw Rectangle
cv2.rectangle(blank, (0,0),(250,250),(0,255,0),2) #-1 for filling the shape
cv2.imshow("Rectangle",blank)

#Draw Cicle
cv2.circle(blank,(250,250),50,(255,0,0),-1)
cv2.imshow("Circle", blank)

#Draw line
cv2.line(blank,(0,0),(250,250),(255,255,0),6)
cv2.imshow("line", blank)

#Put Text
cv2.putText(blank,"Hey Test",(0,255),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),4)
cv2.imshow("Text", blank)

#cv2.imshow("Tesla",img)
cv2.waitKey(0)
