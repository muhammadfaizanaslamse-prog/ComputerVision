import cv2

img = cv2.imread(r"D:\ComputerVision\Data\image.jpg")

img = cv2.resize(img, (700, 500))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges1 = cv2.Canny(blur, 50, 100)
edges2 = cv2.Canny(blur, 100, 200)
edges3 = cv2.Canny(blur, 150, 250)

cv2.imshow("Original", img)
cv2.imshow("Canny 50-100", edges1)
cv2.imshow("Canny 100-200", edges2)
cv2.imshow("Canny 150-250", edges3)

cv2.imwrite(r"D:\ComputerVision\Day10\img_resources\canny_50_100.jpg", edges1)
cv2.imwrite(r"D:\ComputerVision\Day10\img_resources\canny_100_200.jpg", edges2)
cv2.imwrite(r"D:\ComputerVision\Day10\img_resources\canny_150_250.jpg", edges3)

cv2.waitKey(0)
cv2.destroyAllWindows()