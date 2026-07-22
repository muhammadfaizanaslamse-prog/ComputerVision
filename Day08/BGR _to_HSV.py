import cv2
img=cv2.imread(r"D:\ComputerVision\Data\image.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Original",img)
cv2.imshow("Hsv",hsv)
cv2.imwrite(r"D:\ComputerVision\Day08\image_hsv.jpg", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()