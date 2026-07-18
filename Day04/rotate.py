import cv2
img=cv2.imread(r"D:\ComputerVision\Data\image.jpg")
#Rotate the images 
rotate90=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rotate180=cv2.rotate(img,cv2.ROTATE_180)
rotate270=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
#display images
cv2.imshow("Original image",img)
cv2.imshow("Rotate 90°", rotate90)
cv2.imshow("Rotate 180°", rotate180)
cv2.imshow("Rotate 270°", rotate270)
#save the images 
cv2.imwrite(r"D:\ComputerVision\Data\rotate90.jpg",rotate90)
cv2.imwrite(r"D:\ComputerVision\Data\rotate180.jpg",rotate180)
cv2.imwrite(r"D:\ComputerVision\Data\rotate270.jpg",rotate270)
cv2.waitKey(0)
cv2.destroyAllWindows()