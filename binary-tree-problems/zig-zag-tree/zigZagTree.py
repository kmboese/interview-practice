# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# returns a list of children nodes given a parent node, 
def getChildren(parent):
    children = []
    
    if not parent:
        return children
        
    if parent.left:
        children.append(parent.left)
    if parent.right:
        children.append(parent.right)
        
    return children
        
    

# Returns: a list of nodes of each level of a binary tree, in "zig-zag" order.
# Input:
    # A: tree node
    # queue: queue of nodes to get children for
    # zigZagNodes: list of a list of nodes in zig-zag order
    # reverse: whether the children nodes of the nodes in the queue should be appended in reverse
    # order to the zigZagNodes list
def getZigZag(queue, zigZagNodes, reverse):
    children = []
    
    # Base case: queue is empty
    if not queue:
        return zigZagNodes
    
    # Get the children of the current level
    for node in queue:
        tmp = getChildren(node)
        if tmp:
            children.extend(getChildren(node))
    
    # Queue up the children for the next loop
    queue = children
        
    # If no children were added, then we are at the last level and can return
    if not children:
        return zigZagNodes

    # Reverse the children before adding them to the list if needed
    if reverse:
        children = children[::-1]
        
    # Add the children to the list
    zigZagNodes.append(children)
    
    # Alternate the reverse flag
    reverse = not reverse
    
    # Get the next level of children
    getZigZag(queue, zigZagNodes, reverse)
        
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        zigZagNodes = []
        zigZagNodes = getZigZag([A], zigZagNodes, False)
        return(zigZagNodes)
