import numpy as np


def main():
    arr = np.array([1, 2, 3, 4])

    print(arr + 2)  # [3 4 5 6]
    print(arr * 3)  # [3 6 9 12]
    print(arr ** 2)  # [1 4 9 16]

    # Operations between arrays
    arr2 = np.array([10, 20, 30, 40])
    print(arr + arr2)  # [11 22 33 44]


if __name__ == '__main__':
    main()
