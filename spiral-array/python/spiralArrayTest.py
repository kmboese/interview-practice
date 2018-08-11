from spiralArray import *

def main():
    lowerBound = 0
    upperBound = 20
    for i in range(lowerBound,upperBound+1):
        print("Testing spiralArray({})...".format(i))
        matrix = spiral(i)
        printMatrix(matrix)
        matrix.clear()


if __name__ == "__main__":
    main()