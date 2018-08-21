
DEBUG = False
def dPrint(message):
    if DEBUG: print("DEBUG: {}".format(message))

def getMinElements(lists, indices):
    minElements = []
    for i in range(len(indices)):
        # Skip lists that have already been processed completely
        if indices[i] < len(lists[i]):
            # Append the element and its index
            minElements.append((lists[i][indices[i]], i))
    dPrint("minElements: {}".format(minElements))
    return minElements

def findMinElementIndex(lists, indices):
    minElements = getMinElements(lists, indices)
    min = None
    minIndex = None
    for i in range(len(minElements)):
        if min is None or minElements[i][0] < min:
            # Save the minimum value and its index
            min = minElements[i][0]
            minIndex = minElements[i][1]
    
    return minIndex
    


# Merge a list of sorted lists by comparing the smallest element of each list
# per loop, and adding that element to the result array.
# Runtime: # lists = n, total elements = m, then runtime is O(n*m)
def bruteForceMerge(lists):
    sortedList = [] # Master sorted list of all elements
    indices = [0]*len(lists)

    # Loop until all lists have been processed
    while True:
        minElements = getMinElements(lists, indices)
        # Terminate if all lists have been processed
        if not minElements: 
            break
        # Get the index of the minimum element
        minListIndex = findMinElementIndex(lists, indices)
        minList = lists[minListIndex]
        sortedList.append(minList[indices[minListIndex]])
        # Increment the index of the list with the minimum element
        indices[minListIndex] += 1
        #dPrint("Min elements: {}".format(minElements))
        #dPrint("Minimum element list index: {}".format\
            #(findMinElementIndex(lists, indices)))
    return sortedList

def fastMerge(lists):
    return