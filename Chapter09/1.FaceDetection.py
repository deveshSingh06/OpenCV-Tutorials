import cv2

faceCascade = cv2.CascadeClassifier("E:\Github_Projects\OpenCV Tutorials\Resources\haarcascades\haarcascade_frontalface_default.xml")
img = cv2.imread('E:\Github_Projects\OpenCV Tutorials\Resources\people.jpg')
#imgResize = cv2.resize(img, (980, 450))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Detected Faces", img)
cv2.waitKey(0)