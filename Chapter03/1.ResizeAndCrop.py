import cv2
import numpy as np

img = cv2.imread("E:\Github_Projects\OpenCV Tutorials\Resources\lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (400, 300))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)