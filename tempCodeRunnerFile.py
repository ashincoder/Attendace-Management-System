import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Attendance AI', frame)

    # Press q to Quit the Screen
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()