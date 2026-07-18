import cv2
img=cv2.imread(r"D:\ComputerVision\Data\image.jpg")
cv2.imshow("Image",img)
resized=cv2.resize(img,(500,400))
cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()