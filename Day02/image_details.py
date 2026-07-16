import cv2
img=cv2.imread("Resources/image.jpg")
if img is None:
    print("Error:Image not Found")
    exit()

#image dimensions
print("Image Dimensions:",img.shape)
print("Height:",img.shape[0])
print("Widht:",img.shape[1])
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()