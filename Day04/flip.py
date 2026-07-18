import cv2

# Read the image
img = cv2.imread(r"D:\ComputerVision\Data\image.jpg")

# Check if image loaded
if img is None:
    print("❌ Image not found!")
    exit()

# Flip the image
flip_horizontal = cv2.flip(img, 1)
flip_vertical = cv2.flip(img, 0)
flip_both = cv2.flip(img, -1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Horizontal Flip", flip_horizontal)
cv2.imshow("Vertical Flip", flip_vertical)
cv2.imshow("Both Flips", flip_both)

# Save images
cv2.imwrite(r"D:\ComputerVision\Data\flip_horizontal.jpg", flip_horizontal)
cv2.imwrite(r"D:\ComputerVision\Data\flip_vertical.jpg", flip_vertical)
cv2.imwrite(r"D:\ComputerVision\Data\flip_both.jpg", flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()