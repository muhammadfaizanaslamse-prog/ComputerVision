import cv2
import numpy as np

img = cv2.imread(r"D:\ComputerVision\Data\image.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, truncate = cv2.threshold( gray_image,127,255,cv2.THRESH_TRUNC)

cv2.imwrite(r"D:\ComputerVision\Day09\Resources\gray_image.jpg", gray_image)
cv2.imwrite(r"D:\ComputerVision\Day09\Resources\truncate.jpg", truncate)

cv2.imshow("Gray Image", gray_image)
cv2.imshow("Truncate Threshold", truncate)

cv2.waitKey(0)
cv2.destroyAllWindows()