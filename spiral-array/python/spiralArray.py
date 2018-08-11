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
def insertRight(matrix, row, col, i, k):
    for count in range(k):
        matrix[row][count+col] = i
        i += 1
    return matrix, i

def insertLeft(matrix, row, i, n, k):
    for count in range(k):
        # Insert at the given row in reverse order
        matrix[row][(n-k)-count] = i
        i += 1
    return matrix, i

def insertDown(matrix, col, row, i, n, k, MAX_ROW):
    for count in range(k):
        matrix[MAX_ROW-k+count+1][col] = i
        #print("DEBUG: i is {} in insertDown()".format(i))
        i += 1
    return matrix, i

def insertUp(matrix, col, row, i, n, k, MAX_ROW):
    for count in range(k):
        # Insert at the given column in reverse order
        dPrint("in insertUp(): n = {}, k = {}, count = {}".format\
            (n, k, count))
        matrix[(MAX_ROW-row)-count][col] = i
        i += 1
    return matrix, i


def spiral(n):
    # Construct matrix
    matrix = [0]*n
    matrix = initMatrix(matrix, n)
    # Keep track of how many numbers we are inserting into the row
    # or column
    i = 1
    k = n
    upperBound = n*n
    row = 0
    col = 0
    MAX_ROW = n-1
    MAX_COL = n-1

    while i <= upperBound:
        matrix, i = insertRight(matrix, row, col, i, k)
        dPrint("i is {} after insertRight()".format(i))
        k -= 1
        matrix, i = insertDown(matrix, MAX_COL-col, row, i, n, k, MAX_ROW)
        matrix, i = insertLeft(matrix, MAX_ROW-row, i, n, k)
        k -= 1
        row += 1
        matrix, i = insertUp(matrix, col, row, i, n, k, MAX_ROW)
        #k -= 1
        col += 1
        #print("i is {} after insertDown()".format(i))
        #insertLeft(matrix, MAX_row-row, i, k)
        #print("i before the break is {}".format(i))


    return matrix