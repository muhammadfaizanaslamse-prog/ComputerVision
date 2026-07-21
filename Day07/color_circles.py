import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)

cv2.imshow("Image", img)
#icrct
cv2.circle(img,(50,225),30,(255,0,0),-2)
cv2.circle(img,(200,225),30,(0,255,0),-2)
cv2.circle(img,(350,225),30,(0,0,255),-2)
print(img.shape)
cv2.imshow("Circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()