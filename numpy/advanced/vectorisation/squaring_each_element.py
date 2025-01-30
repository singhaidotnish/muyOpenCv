import numpy as np

# ❌ Using Loops (Slow)
arr = np.array([1, 2, 3, 4, 5])

result = []
for x in arr:
    result.append(x ** 2)

print(result)  # [1, 4, 9, 16, 25]


# ✅ Using NumPy Vectorization (Fast)

result = arr ** 2
print(result)  # [ 1  4  9 16 25]
