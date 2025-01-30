import cv2
import numpy as np


# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)
cv2.line(canvas, (50, 50), (450, 450), (0, 255, 0), 5)  # (start, end, color, thickness)
cv2.imshow("Line", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
