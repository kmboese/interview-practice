from searchRange import *

def main():
    # nums = [1,3,5,5,5,5,6,7,9,13,14,16,22,23,25,29,33,35,36,37]
    # key =  1
    nums = [1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,5,5,5,5,5,\
    6,6,6,7,7,8,8,8,8,9,9,10,10,10]
    key = 4
    print("Nums has {} elements".format(len(nums)))
    index = binarySearch(nums, key)
    leftMost = scanLeft(nums, nums[index], index)
    rightMost = scanRight(nums, nums[index], index)

    # Print results
    if index != -1:
        print("Key of {} found at index {} in list".format\
        (key, index))
        print("leftmost occurrence of {} is at index {}".format\
            (key, leftMost))
        print("rightmost occurrence of {} is at index {}".format\
            (key, rightMost))
    else:
        print("Key not found!")

    

if __name__ == "__main__":
    main()