import cv2

# 1.Reading an Image

img = cv2.imread("Muscle-names-3.png")

cv2.imshow("Output", img)
cv2.waitKey(0) # 0 means infinitely long, whereas any other value such as 1000 means 1 second.