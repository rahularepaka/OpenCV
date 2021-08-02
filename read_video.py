import cv2

cap = cv2.VideoCapture(0) #Replace 0/1/2 with file path of the video

while True:
    ret, frame = cap.read()
    
    cv2.imshow("Video",frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
