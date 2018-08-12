class Node:
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None

DEBUG = True
total = 0

def dPrint(message):
    if DEBUG: print("DEBUG: " + message)

def isLeaf(node):
    if not node or node.left or node.right:
        return False
    else:
        return True

def traverse(node, numString, total):
    if not node:
        return total
    if numString:
        tmp = numString + str(node.val)
    else:
        tmp = str(node.val)
    dPrint("node value is {}, tmp is {}".format(node.val,tmp))
    # Add to sum if leaf node
    if isLeaf(node):
        total += int(tmp)
        dPrint("isLeaf(): total is {}, numString is {}".format(total,tmp))
        #tmp = numString[:len(numString)-1]
        return total
    if node.left:
        #dPrint("Before traversal: total is {}".format(total))
        total = traverse(node.left, tmp, total)
    if node.right:
        #dPrint("Before traversal: total is {}".format(total))
        total = traverse(node.right, tmp, total)
    
    return total

def sumNumbers(root):
    total = traverse(root, "", 0)
    print("Original total is {}".format(total))
    return (total % 1003)