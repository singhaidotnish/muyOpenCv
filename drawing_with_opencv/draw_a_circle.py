import cv2
import numpy as np


# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.circle(canvas, (250, 250), 100, (0, 255, 255), -1)  # (center, radius, color, thickness)
cv2.imshow("Circle", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 🔹 (0, 255, 255) → Yellow color
# 🔹 Radius = 100 pixels