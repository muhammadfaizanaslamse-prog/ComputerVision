import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.line(img, (0,0), (512,512), (255,0,0), 3)

cv2.rectangle(img, (50,50), (250,200), (0,255,0), 2)

cv2.circle(img, (350,150), 50, (0,255,0), cv2.FILLED)

cv2.putText(
    img,#image
    "Day 3",#text
    (350,450),#position
    cv2.FONT_HERSHEY_SIMPLEX,#font
    2,#fontscale
    (255,255,255),#color
    3#thickness
)

cv2.imshow("Drawing", img)

cv2.waitKey(0)
cv2.destroyAllWindows()