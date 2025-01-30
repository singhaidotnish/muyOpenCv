import cv2
import numpy as np


# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.putText(canvas, "Hello, OpenCV!", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow("Text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 🔹 (50, 250) → Bottom-left corner
# 🔹 Font: cv2.FONT_HERSHEY_SIMPLEX
# 🔹 Size: 1
# 🔹 Thickness: 2