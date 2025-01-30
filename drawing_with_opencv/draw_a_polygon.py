import cv2
import numpy as np


# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

pts = np.array([[100, 50], [200, 300], [400, 200], [300, 50]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(canvas, [pts], isClosed=True, color=(0, 165, 255), thickness=3)
cv2.imshow("Polygon", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 🔹 isClosed=True → Closes the shape
# 🔹 (0, 165, 255) → Orange color