import cv2


cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    cv2.imshow('OUTPUT', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
