import numpy as np

def main():
    arr = np.array([10, 20, 30, 40, 50])

    filtered = arr[arr > 25]  # Get elements greater than 25
    print(filtered)  # [30, 40, 50]



if __name__ == '__main__':
    main()
