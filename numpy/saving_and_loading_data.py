import numpy as np

def main():
    arr = np.array([10, 20, 30, 40, 50])
    np.save("my_array.npy", arr)  # Save array
    loaded_arr = np.load("my_array.npy")  # Load array
    print('loaded arr ', loaded_arr)


if __name__ == '__main__':
    main()
