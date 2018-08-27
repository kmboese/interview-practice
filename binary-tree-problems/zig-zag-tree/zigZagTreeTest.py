from zigZagTree import getZigZag, Node

def main():
    A = Node(1)
    # Level 1
    A.left = Node(6)
    A.right = Node(7)
    # Level 2
    A.left.left = Node(10)
    A.left.right = Node(11)
    zigZagNodes = []
    zigZagNodes = getZigZag([A], zigZagNodes, False)

    # Print results
    for values in zigZagNodes:
        for value in values:
            print("Node: {}".format(value))


if __name__ == "__main__":
    main()