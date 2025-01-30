import numpy as np

arr = np.array([1, 2, 3, 4])
scalar = 10

result = arr + scalar  # Broadcasting happens here
print(result)  # Output: [11 12 13 14]
