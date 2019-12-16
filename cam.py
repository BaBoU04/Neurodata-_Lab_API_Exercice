import cv2

cap = cv2.VideoCapture(0)

#Get first frame from webcam stream
ret, frame = cap.read()

#Check that webcam works normally and nobody stopped the system
while ret:
    cv2.imshow('webcam', frame)
    # Wait 50ms for any key pressed. Stops system if 'q' was pressed
    if cv2.waitKey(50) & 0xff == ord('q'):
        break
    # Read next frame
    ret, frame = cap.read()

# Release webcam
cap.release()