import cv2
img=cv2.imread(r"D:\ComputerVision\Data\image.jpg")
cv2.imshow("Original Image",img)
crop=img[100:300,150:400]
cv2.imshow("Cropped Image",crop)
print(crop.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()