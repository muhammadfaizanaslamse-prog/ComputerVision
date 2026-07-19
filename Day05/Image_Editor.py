import cv2


# ==========================
# 1. Load Image
# ==========================

image = cv2.imread("sample.jpg")


# Check image
if image is None:
    print("Image not found!")
    exit()


print("Image loaded successfully")


# ==========================
# 2. Display Original Image
# ==========================

cv2.imshow(
    "Original Image",
    image
)


# ==========================
# 3. Convert Image to Grayscale
# ==========================

gray_image = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)


cv2.imshow(
    "Gray Image",
    gray_image
)


# ==========================
# 4. Blur Image
# ==========================

blur_image = cv2.GaussianBlur(
    image,
    (15, 15),
    0
)


cv2.imshow(
    "Blur Image",
    blur_image
)


# ==========================
# 5. Edge Detection
# ==========================

edges = cv2.Canny(
    gray_image,
    100,
    200
)


cv2.imshow(
    "Edge Detection",
    edges
)


# ==========================
# 6. Resize Image
# ==========================

resize_image = cv2.resize(
    image,
    (500, 500)
)


cv2.imshow(
    "Resized Image",
    resize_image
)


# ==========================
# 7. Flip Image
# ==========================

flip_image = cv2.flip(
    image,
    1
)


cv2.imshow(
    "Flipped Image",
    flip_image
)


# ==========================
# 8. Save Edited Images
# ==========================

cv2.imwrite(
    "gray_image.jpg",
    gray_image
)

cv2.imwrite(
    "blur_image.jpg",
    blur_image
)

cv2.imwrite(
    "edge_image.jpg",
    edges
)


print("Edited images saved successfully!")


# ==========================
# 9. Close Program
# ==========================

cv2.waitKey(0)

cv2.destroyAllWindows()