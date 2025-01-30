import numpy as np

def main():
    arr2 = np.array([[10, 20, 30], [40, 50, 60]])

    print(arr2[0, 1])  # First row, second column (20)
    print(arr2[:, 1])  # All rows, second column ([20, 50])
    print(arr2[1, :])  # Second row ([40, 50, 60])



if __name__ == '__main__':
    main()
