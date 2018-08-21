# Given an input size, print a square matrix that prints integers in a 
# spiral pattern.
# Ex: 
# input = 3
# 1 2 3 
# 8 9 4
# 7 6 5
# Pattern:
# ---->
#^--->|
#|    |
#|    v
#<-----
DEBUG = False

def dPrint(message):
    if DEBUG: print("DEBUG: " + message)

def initMatrix(matrix, n):
    for i in range(n):
        matrix[i] = [0]*n
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:4} ".format(matrix[i][j]),end='')
        print()

# insert a row into a matrix, zero-indexed
def insertRight(matrix, top, left, right, i):
    for index in range(left, right+1):
        dPrint("index = {}".format(index))
        matrix[top][index] = i
        i += 1
    return matrix, i

def insertLeft(matrix, bottom, left, right, i):
    # Insert at the given row in reverse order
    for index in range(right, left-1, -1):
        matrix[bottom][index] = i
        i += 1
    return matrix, i

def insertDown(matrix, right, top, bottom, i):
    for index in range(top, bottom+1):
        matrix[index][right] = i
        i += 1
    return matrix, i

def insertUp(matrix, left, top, bottom, i):
    # Insert at the given column in reverse order
    dPrint("bottom = {}, top+1 = {}".format(bottom, top+1))
    for index in range(bottom, top-1, -1):
        matrix[index][left] = i
        i += 1
    return matrix, i


def spiral(n):
    # Error handling
    if (n <= 0):
        print("Error in spiral(): n must be greater than zero.")
        return []
    # Construct matrix
    matrix = [0]*n
    matrix = initMatrix(matrix, n)
    # Keep track of how many numbers we are inserting into the row
    # or column
    i = 1
    k = n
    upperBound = n*n

    # Matrix boundaries
    top = 0
    bottom = n-1
    left = 0
    right = n-1

    while i <= upperBound:
        dPrint("Inserting right, i = {}".format(i))
        matrix, i = insertRight(matrix, top, left, right, i)
        top += 1

        dPrint("Inserting down, i = {}".format(i))
        matrix, i = insertDown(matrix, right, top, bottom, i)
        right -= 1

        dPrint("Inserting left, i = {}".format(i))
        matrix, i = insertLeft(matrix, bottom, left, right, i)
        bottom -= 1

        dPrint("Inserting up, i = {}".format(i))
        matrix, i = insertUp(matrix, left, top, bottom, i)
        left += 1
        dPrint("End of loop, i = {}".format(i))

    return matrix