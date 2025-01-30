import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
B = np.array([10, 20, 30])  # Shape: (1, 3)

result = A + B  # B is "stretched" to match A
print(result)
