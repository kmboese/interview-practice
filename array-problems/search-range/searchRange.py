from math import ceil

DEBUG = True

def dPrint(message):
    if DEBUG: print("DEBUG: {}".format(message))

# Given a sorted list, finds the given element in O(log n) time.
# Returns: the midpoint of the first occurance of the key in the list
# if it exists, or -1 otherwise 
def binarySearch(nums, key):
    count = 1 # keep track of iterations
    first = 0
    last = len(nums)-1
    found = False
    # Check for invalid input
    if not nums or not key:
        dPrint("Looped {} times, didn't find the key".format(count))
        return -1
    # Check if number is within bounds of sorted list
    if key < nums[0] or key > nums[len(nums)-1]:
        dPrint("Looped {} times, didn't find the key".format(count))
        return -1
    # Initialize the partition to be half the list size
    partitionSize = len(nums) // 2 

    while first<=last and not found:
        midpoint = (first+last)//2

        # If we found the key, return it
        if nums[midpoint] == key:
            dPrint("Looped {} times to find the key".format(count))
            found = True
        else:
            # Look in left half
            if nums[midpoint] > key:
                last = midpoint-1
            # Look in right half
            else:
                first = midpoint+1
        count += 1

    if found:
        return midpoint
    else:
        return -1
    
    # If we exit the loop, we didn't find the key
    dPrint("Looped {} times, didn't find the key".format(count))
    return -1

# Returns the leftmost occurrence of a key in a sorted list
def scanLeft(nums, key, midpoint):
    # Check for invalid input
    if nums[midpoint] != key:
        return None

    while midpoint >= 0 and nums[midpoint] == key:
        midpoint -= 1

    return midpoint+1

# Returns the rightmost occurrence of a key in a sorted list
def scanRight(nums, key, midpoint):
    # Check for invalid input
    if nums[midpoint] != key:
        return None

    while midpoint < len(nums) and nums[midpoint] == key:
        midpoint += 1

    return midpoint-1