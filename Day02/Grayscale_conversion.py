import cv2

# Read image from the same folder as this Python file
img = cv2.imread("image.jpg")

# Check if image loaded successfully
if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show grayscale image
cv2.imshow("Gray Image", gray)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()