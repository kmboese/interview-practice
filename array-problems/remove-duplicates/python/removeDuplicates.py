def removeDuplicates(array):
    ret = []
    hashTable = {} # Keep track of elements that exist

    for num in array:
        if not hashTable.get(num):
            hashTable[num] = True
            ret.append(num)

    return ret