import cv2
import numpy as np

# Create a black image (height=500, width=500)
img = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.imshow("Black Image", img)
cv2.line(img,(50,50),(300,300),(0,255,0),5)
cv2.imshow("lINE",img)
cv2.rectangle(img,(50,50),(350,350),(0,0,255),5)
cv2.imshow("Rectangle",img)
cv2.circle(img,(250,250),100,(255,0,0),5)
cv2.imshow("Circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()