from zigZagTree import getZigZag, Node

def main():
    A = Node(1)
    zigZagNodes = []
    zigZagNodes = getZigZag([A], zigZagNodes, False)

    # Print results
    print(zigZagNodes)


if __name__ == "__main__":
    main()