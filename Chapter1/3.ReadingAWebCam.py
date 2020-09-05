import cv2

# 3. Reading from a WebCam

frameWidth = 940
frameHeight = 580
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
#cap.set(10,150)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


