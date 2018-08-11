from spiralArray import *

def main():
    lowerBound = 1
    upperBound = 6
    for i in range(lowerBound,upperBound):
        print("Testing spiralArray({})...".format(i))
        matrix = spiral(i)
        printMatrix(matrix)
        matrix.clear()


if __name__ == "__main__":
    main()