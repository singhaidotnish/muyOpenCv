import numpy as np

def main():
    np.random.seed(42)  # Set seed for reproducibility

    print(np.random.rand(3))  # 3 random numbers between 0 and 1
    print(np.random.randint(10, 50, (2, 2)))  # 2x2 matrix of random integers from 10 to 50



if __name__ == '__main__':
    main()
    