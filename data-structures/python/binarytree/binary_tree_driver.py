# from binarytree import BinaryTree
from balanced_binary_tree import BalancedBinaryTree, Node

NUM_NODES = 10

def main():
    start_num = 1
    binary_tree = BalancedBinaryTree()
    binary_tree.insert(1)

    # Generate tree
    for i in range(start_num+1, NUM_NODES):
        binary_tree.insert(i)

    binary_tree.print_tree()
    print(f'Binary tree height: {binary_tree.get_height()}')

if __name__ == '__main__':
    main()