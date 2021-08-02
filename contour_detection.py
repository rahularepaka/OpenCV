import cv2
import numpy as np

img = cv2.imread("Photos\\minecraft.png")
cv2.imshow("Original",img)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank', blank)

grayscale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", grayscale_img)

blur = cv2.GaussianBlur(grayscale_img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

canny = cv2.Canny(blur,5,80)
cv2.imshow("Canny", canny)

#thresholding
#ret, thresh = cv2.threshold(grayscale_img, 125, 255, cv2.THRESH_BINARY)
#cv2.imshow('Thresh', thresh)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow('Contours Drawn', blank)


cv2.waitKey(0)
