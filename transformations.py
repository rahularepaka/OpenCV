import cv2
import numpy as np

img = cv2.imread("Photos\\arduino.jpg")

cv2.imshow("image",img)

#Translation
def translate(img,x,y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img,100,100)
cv2.imshow("translate",translated)

#Rotation
def rotate(img,angle,rotpoint=None):
    (height,width) = img.shape[:2]
    
    if rotpoint is None:
        rotpoint = (width//2,height//2)
        
    rotMat = cv2.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,45)
cv2.imshow("Rotate",rotated)

#flipping
fliped = cv2.flip(img,0)
cv2.imshow("flip",fliped)


cv2.waitKey(0)
