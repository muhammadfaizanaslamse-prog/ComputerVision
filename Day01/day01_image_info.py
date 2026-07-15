import cv2

image = cv2.imread("image.jpg")

print("Height :", image.shape[0])
print("Width  :", image.shape[1])
print("Channels:", image.shape[2])