import numpy as np

def main():
    arr = np.array([1, 2, 3, 4, 5])

    print(np.sum(arr))  # Sum of elements (15)
    print(np.mean(arr))  # Mean (3.0)
    print(np.max(arr))  # Maximum value (5)
    print(np.min(arr))  # Minimum value (1)
    print(np.std(arr))  # Standard deviation


if __name__ == '__main__':
    main()
