from sumRootLeaf import *

def testSmall():
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(0)
    root.right.left = Node(1)
    root.right.right.left = Node(7)
    root.right.right.right = Node(0)

    total = sumNumbers(root)
    print("Total is {}".format(total))

def main():
    testSmall()

if __name__ == "__main__":
    main()