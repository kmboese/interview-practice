class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'

def is_leaf(node: Node):
    return not node.left and not node.right


class BalancedBinaryTree:
    def __init__(self):
        self.root = None

    def get_height(self, height: int=0, node: Node=None):
        # Special case: start from the root
        if not node:
            return self.get_height(1, self.root)

        if node.left:
            return self.get_height(height+1, node.left)
        elif node.right:
            return self.get_height(height+1, node.right)
        else:
            return height

    def insert_balanced(self, value: int, nodes: list[Node]=None):
        if nodes is None:
            if not self.root:
                debug(f'Assigning root node value={value}')
                self.root = Node(value)
                return
            else:
                self.insert_balanced(value, [self.root])
                return

        next_nodes = []
        for node in nodes:
            if node.left and node.right:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
            elif not node.left:
                debug(f'Left-assigning value={value} to node={node.value}')
                node.left = Node(value)
                return
            else:
                debug(f'Right-assigning value={value} to node={node.value}')
                node.right = Node(value)
                return
        if next_nodes:
            self.insert_balanced(value, next_nodes)

    def traverse_balanced_in_order(self, depth=0, nodes_to_traverse=None, all_nodes=None):
        debug(f'Calling traverse_balanced_in_order: depth={depth}, nodes_to_traverse={nodes_to_traverse}, all_nodes={all_nodes}')
        if all_nodes is None:
            if not self.root:
                return
            else:
                return self.traverse_balanced_in_order(0, [self.root], [])

        next_nodes = []
        for node in nodes_to_traverse:
            all_nodes.append(node)
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        if next_nodes:
            debug(f'Recursing: depth={depth+1}, nodes_to_traverse={next_nodes}, all_nodes={all_nodes}')
            return self.traverse_balanced_in_order(depth + 1, next_nodes, all_nodes)
        else:
            debug(f'Returning: all_nodes={all_nodes}')
            return all_nodes

    def print_balanced_in_order(self, depth=0, nodes=None):
        if nodes is None:
            if not self.root:
                return
            else:
                self.print_balanced_in_order(0, [self.root])
                return

        next_nodes = []
        indent = f'\t'*depth
        for node in nodes:
            print(f'{indent}{node.value}')
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        if next_nodes:
            self.print_balanced_in_order(depth + 1, next_nodes)


    def insert(self, value: int, node: Node=None) -> None:
        if not node:
            if not self.root:
                self.root = Node(value)
                return
            else:
                self.insert(value, self.root)
                return

        if not node.left:
            debug(f'Left-inserting value {value} under node {node.value}')
            node.left = Node(value)
            return
        elif not node.right:
            debug(f'Right-inserting value {value} under node {node.value}')
            node.right = Node(value)
            return
        else:
            self.insert(value, node.left)

    def get_values_inorder(self, node: Node=None, values: list=None):
        if not node and not values:
            return self.get_values_inorder(self.root, [])

        if node.left:
            self.get_values_inorder(node.left, values)
        if node.right:
            self.get_values_inorder(node.right, values)
        debug(f'Found node with value {node.value}')
        values.append(node.value)

        return values

    def get_values_inorder_old(self, node: Node=None, values: list=None):
        if not node and not values:
            return self.get_values_inorder_old(self.root, [])

        if node.left:
            values.append(self.get_values_inorder_old(node.left, values))
        values.append(node.value)
        if node.right:
            values.append(self.get_values_inorder_old(node.right, values))
        values.append(node.value)
        return values


    def print_tree(self, depth: int=None, node: Node = None,):
        if not node:
            print(self.root.value)
            self.print_tree(1, self.root)
            return

        indent = f'\t'*depth
        if node.left:
            debug('Printing left')
            print(f'{indent}{node.left.value}')
            self.print_tree(depth+1, node.left)
        if node.right:
            debug('Printing right')
            print(f'{indent}{node.right.value}')
            self.print_tree(depth+1, node.right)
        if not node.left and not node.right:
            debug('Hit leaf')
            return


def debug(message: str):
    print(f'DEBUG: {message}')






