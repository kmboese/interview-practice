# from binarytree import BinaryTree
from balanced_binary_tree import *

NUM_NODES = 10

def main():
    start_num = 1
    binary_tree = BalancedBinaryTree()

    # Generate tree
    for i in range(start_num, NUM_NODES+start_num):
        binary_tree.insert_balanced(i)

    print('Pre-order traversal:')
    pre_order_traversal(binary_tree.root)
    print('In-order traversal: ')
    in_order_traversal(binary_tree.root)
    print('Post-order traversal: ')
    post_order_traversal(binary_tree.root)
    print('BFS traversal: ')
    bfs_traversal([binary_tree.root])

if __name__ == '__main__':
    main()