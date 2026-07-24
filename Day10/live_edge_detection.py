import cv2

# Open webcam
cam = cv2.VideoCapture(0)


if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read frame
    success, frame = cam.read()

    if not success:
        print("Failed to capture frame.")
        break

    frame = cv2.resize(frame, (700, 500))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 100, 200)

    cv2.imshow("Original Webcam", frame)
    cv2.imshow("Gray", gray)
    cv2.imshow("Blur", blur)
    cv2.imshow("Edges", edges)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()