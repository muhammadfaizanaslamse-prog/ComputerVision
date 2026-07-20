import cv2
img=cv2.imread(r"D:\ComputerVision\Data\image.jpg")
cv2.imshow("Original Image",img)
print(img.shape)
reszie=cv2.resize(img,(150,350))
cv2.imshow("Resized Image",reszie)
cv2.waitKey(0)
cv2.destroyAllWindows()