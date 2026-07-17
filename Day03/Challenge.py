import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# 😊 Smiley Face
# Face
cv2.circle(img, (256, 120), 60, (0, 255, 255), cv2.FILLED)

# Eyes
cv2.circle(img, (235, 100), 6, (0, 0, 0), cv2.FILLED)
cv2.circle(img, (277, 100), 6, (0, 0, 0), cv2.FILLED)

# Smile
cv2.ellipse(img, (256, 130), (25, 15), 0, 0, 180, (0, 0, 0), 2)

# Name
cv2.putText(
    img,
    "Faizan Aslam",
    (120, 250),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

# Rectangle
cv2.rectangle(
    img,
    (150, 320),   # Top-left corner
    (360, 430),   # Bottom-right corner
    (0, 255, 0),  # Green
    3             # Thickness
)

# Optional text inside rectangle
cv2.putText(
    img,
    "Rectangle",
    (175, 385),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2
)

# Display image
cv2.imshow("Day 3 Challenge", img)

cv2.waitKey(0)
cv2.destroyAllWindows()