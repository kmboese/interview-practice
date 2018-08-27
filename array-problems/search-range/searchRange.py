from math import ceil

DEBUG = True

def dPrint(message):
    if DEBUG: print("DEBUG: {}".format(message))

# Given a sorted list, finds the given element in O(log n) time.
# Returns: the index of the first occurance of the key in the list
# if it exists, or -1 otherwise 
def binarySearch(nums, key):
    count = 1 # keep track of iterations
    lookLeft = False
    lookRight = False
    # Check for invalid input
    if not nums or not key:
        dPrint("Looped {} times, didn't find the key".format(count))
        return -1
    # Check if number is within bounds of sorted list
    if key < nums[0] or key > nums[len(nums)-1]:
        dPrint("Looped {} times, didn't find the key".format(count))
        return -1
    # Initialize the search to be the middle of the list
    index = len(nums) // 2
    # Initialize the partition to be half the list size
    partitionSize = len(nums) // 2 

    while index >= 0 and index < len(nums):
        # If we found the key, return it
        if nums[index] == key:
            dPrint("Looped {} times to find the key".format(count))
            return index

        # Cut the partition in half before searching again
        if partitionSize != 1:
            partitionSize = (partitionSize//2)

        # If the index value is greater than the key, 
        # look left
        if nums[index] > key:
            dPrint(str(nums[index]))
            if partitionSize == 1:
                lookLeft = True
            index -= partitionSize

        # Else if the index value is less than the key, look right
        else:
            dPrint(str(nums[index]))
            if partitionSize == 1:
                lookRight = True
            index += partitionSize

        # If the partition size becomes 0, then we have stopped making
        # progress and need to terminate the loop
        if lookLeft and lookRight:
            break
        count += 1
    
    # If we exit the loop, we didn't find the key
    dPrint("Looped {} times, didn't find the key".format(count))
    return -1

# Returns the leftmost occurrence of a key in a sorted list
def scanLeft(nums, key, index):
    # Check for invalid input
    if nums[index] != key:
        return None

    while index >= 0 and nums[index] == key:
        index -= 1

    return index+1

# Returns the rightmost occurrence of a key in a sorted list
def scanRight(nums, key, index):
    # Check for invalid input
    if nums[index] != key:
        return None

    while index < len(nums) and nums[index] == key:
        index += 1

    return index-1