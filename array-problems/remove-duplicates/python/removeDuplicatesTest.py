from random import random
from removeDuplicates import removeDuplicates

def main():
    nums = [1,2,3,4,5,5,5,5,5]
    print("Removing duplicates: ")
    uniqueNums = removeDuplicates(nums)

    print("Original list: {}\nList with no duplicates: {}"\
        .format(nums, uniqueNums))
    print("Original list had {} elements\nNew list has {} elements"\
        .format(len(nums), len(uniqueNums)))
    return

if __name__ == "__main__":
    main()