import cv2
import numpy as np

img = np.zeros((200, 500, 3), dtype=np.uint8)

cv2.putText(
    img,
    "Faizan Aslam",
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.,
    (255, 255, 255),
    3
)

cv2.imshow("My Name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
