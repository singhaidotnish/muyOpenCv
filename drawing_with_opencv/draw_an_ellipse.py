import cv2
import numpy as np


# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.ellipse(canvas, (250, 250), (150, 100), 0, 0, 360, (255, 0, 255), 3)
cv2.imshow("Ellipse", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

#
# 🔹 (150, 100) → Width and height of the ellipse
# 🔹 0 to 360 → Full ellipse

cv2.ellipse(canvas, (250, 250), (150, 100), 0, 0, 180, (255, 255, 0), 3)
# ✅ Partial Ellipse (Arc Example)
# 🟢 Draws only the top half!