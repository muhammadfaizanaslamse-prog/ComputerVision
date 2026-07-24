import cv2

img = cv2.imread(r"D:\ComputerVision\Data\image.jpg")

img = cv2.resize(img, (700, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 100, 200)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.imwrite(r"D:\ComputerVision\Day10\img_resources\original.jpg", img)
cv2.imwrite(r"D:\ComputerVision\Day10\img_resources\gray.jpg", gray)
cv2.imwrite(r"D:\ComputerVision\Day10\img_resources\blur.jpg", blur)
cv2.imwrite(r"D:\ComputerVision\Day10\img_resources\edges.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()