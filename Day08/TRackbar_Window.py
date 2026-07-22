import cv2
def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 600, 300)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
while True:
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    print("Hue Min:", h_min, "Hue Max:", h_max)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()