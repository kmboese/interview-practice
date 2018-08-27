from mergeSortedArrays import *
from random import randint

divider = "\n__________________________________________________\n"

def testBruteForceMerge():
    print("***** testBruteForceMerge() *****" + divider)
    listNum = 10
    listSize = 5
    lists = []
    sortedList = []
    
    for i in range(0,listNum):
        # Generate a list
        lst = []
        for i in range(0,listSize):
            lst.append(randint(0,listNum*5))
        # Sort the list
        lst.sort()
        # Append the list
        lists.append(lst)
    print("Test: lists = {}".format(lists))
    sortedList = bruteForceMerge(lists)
    print("Sorted list: {}".format(sortedList))


def main():
    testBruteForceMerge()

if __name__ == "__main__":
    main()