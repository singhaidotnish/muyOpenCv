import numpy as np

def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print(A @ B)  # Matrix multiplication
    print(np.linalg.inv(A))  # Inverse of a matrix
    print(np.linalg.det(A))  # Determinant of a matrix



if __name__ == '__main__':
    main()
    