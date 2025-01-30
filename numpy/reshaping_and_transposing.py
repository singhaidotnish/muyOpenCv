import numpy as np


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    print(arr.T)  # Transpose
    print(arr.reshape(3, 2))  # Reshape into 3 rows, 2 columns


if __name__ == '__main__':
    main()
    