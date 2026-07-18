import cv2
img=cv2.imread(r"D:\ComputerVision\Data\image.jpg")
crop=img[100:400,150:400]
cv2.imshow("Original Image",img)
cv2.imshow("Cropped Image",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()