import cv2

img = cv2.imread(r"D:\ComputerVision\Data\image.jpg")

horizontal = cv2.flip(img, 1)
vertical = cv2.flip(img, 0)
both = cv2.flip(img, -1)

cv2.imshow("Horizontal", horizontal)
cv2.imshow("Vertical", vertical)
cv2.imshow("Both", both)

cv2.waitKey(0)
cv2.destroyAllWindows()