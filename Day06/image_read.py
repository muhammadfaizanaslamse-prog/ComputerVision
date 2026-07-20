import cv2 
img=cv2.imread(r"D:\ComputerVision\Data\image.jpg")
print(img.shape)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()