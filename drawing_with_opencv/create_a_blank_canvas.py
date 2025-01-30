import cv2
import numpy as np

# Create a black image (height=500, width=500, 3 color channels)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

# Display the canvas
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
