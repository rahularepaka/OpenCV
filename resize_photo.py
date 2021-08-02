import cv2

img = cv2.imread("Photos\\tesla.jpg")

scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


cv2.imshow("Image", resized)
cv2.waitKey(0)
