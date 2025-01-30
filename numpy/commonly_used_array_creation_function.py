import numpy as np


def main():

    # 2D array (3 rows, 4 columns) filled with zeros
    zeros = np.zeros((3, 4))

    # 2D array (2 rows, 1 columns) filled with ones
    ones = np.ones((2, 1))

    # Create an array with a range of values
    range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

    # Create an array of equally spaced numbers
    linspace_arr = np.linspace(0, 10, 5)  # 5 points between 0 and 10

    # Create an identity matrix
    identity_matrix = np.eye(3)  # 3x3 identity matrix

    print(zeros, ones, range_arr, linspace_arr, identity_matrix, sep="\n")
    # print(zeros, ones)


if __name__ == '__main__':
    main()
