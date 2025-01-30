import cv2
import numpy as np


# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.line(canvas, (50, 50), (450, 450), (0, 255, 0), 5)
cv2.rectangle(canvas, (100, 100), (400, 400), (255, 0, 0), 3)
cv2.circle(canvas, (250, 250), 100, (0, 255, 255), -1)
cv2.putText(canvas, "OpenCV Drawing!", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Drawing", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
