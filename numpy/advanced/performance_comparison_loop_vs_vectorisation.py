import numpy as np


# Using Loops (Slow)

import time

arr = np.random.randint(1, 100, size=1000000)  # 1 Million elements

start = time.time()
squared = [x ** 2 for x in arr]  # Squaring each element
end = time.time()

print("Loop Execution Time:", end - start)


# Using NumPy Vectorization (Fast)

start = time.time()
squared = arr ** 2
end = time.time()

print("NumPy Execution Time:", end - start)



