import cv2

image = cv2.imread("image.jpg")

cv2.imwrite("saved_image.jpg", image)

print("Image saved successfully!")