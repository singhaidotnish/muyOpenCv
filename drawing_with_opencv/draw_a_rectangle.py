import cv2
import numpy as np


# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.rectangle(canvas, (100, 100), (400, 400), (255, 0, 0), 3)  # (top-left, bottom-right, color, thickness)
cv2.imshow("Rectangle", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ✅ Use -1 for a filled rectangle:
cv2.rectangle(canvas, (150, 150), (350, 350), (0, 0, 255), -1)
