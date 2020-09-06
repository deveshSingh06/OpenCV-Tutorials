import cv2

# 2.Reading a Video

frameWidth = 940
frameHeight = 680
cap = cv2.VideoCapture("handwritingFinal.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break