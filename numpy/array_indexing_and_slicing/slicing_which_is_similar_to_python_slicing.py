import numpy as np


def main():
    arr = np.array([10, 20, 30, 40, 50])
    print(arr[1:4])  # Elements from index 1 to 3
    print(arr[:3])  # First 3 elements
    print(arr[::2])  # Every second element


if __name__ == '__main__':
    main()
