import cv2

img = cv2.imread("Photos\\arduino.jpg")

#convert to Grayscale
grayscale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image-Gray", grayscale_img)

#Blur
blur = cv2.GaussianBlur(img,(7,7), cv2.BORDER_DEFAULT)
cv2.imshow("Blured",blur)

#edge casace - canny edge detection
canny = cv2.Canny(blur,25,80)
cv2.imshow("Canny",canny)

#dilating the img
dilated = cv2.dilate(canny,(3,3),iterations=1)
cv2.imshow("dilated",dilated)

#eroding
eroded = cv2.erode(dilated,(3,3),iterations=1)
cv2.imshow("eroded",eroded)

#Resize-CBO
resized = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("reize",resized)
 
#Crop
cropped = img[50:200,200:400]
cv2.imshow("Crop",cropped)

cv2.imshow("Image",img)
cv2.waitKey(0)
