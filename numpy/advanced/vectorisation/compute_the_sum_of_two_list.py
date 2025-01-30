import numpy as np

# ❌ Using a Loop
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = [x + y for x, y in zip(list1, list2)]
print(result)  # [11, 22, 33, 44, 55]

# ✅ Using NumPy Vectorization
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

result = arr1 + arr2
print(result)  # [11 22 33 44 55]
