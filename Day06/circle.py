import cv2

img = cv2.imread(r"D:\ComputerVision\Data\image.jpg")
cv2.circle(
    img,
    (300, 200),
    60,
    (255, 0, 0),
    3
)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()