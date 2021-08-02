import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    resized = cv2.resize(frame,(500,500),cv2.INTER_AREA)
    
    cv2.imshow('Video-Orginal',frame)
    cv2.imshow('Video-Smaller',resized)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    