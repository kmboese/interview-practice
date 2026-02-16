from unittest import TestCase
from balanced_binary_tree import *

class TestBinaryTree(TestCase):

    def test_create(self):
        value = 5
        binary_tree = BalancedBinaryTree()
        binary_tree.insert(value)
        self.assertEqual(value, binary_tree.root.value)

    def test_insert_order(self):
        #       1
        #   2       3
        # 4   5    6  7
        binary_tree = BalancedBinaryTree()
        start_num = 1
        num_nodes = 6
        generated_node_values = [i for i in range(start_num, start_num + num_nodes)]
        expected_order = [4, 5, 2, 1, 3, 6]

        for node_value in generated_node_values:
            binary_tree.insert(node_value)

        actual_node_values = binary_tree.get_values_inorder()
        self.assertEqual(expected_order, actual_node_values)

    def test_insert_balanced(self):
        # Arrange

        #       1
        #   2       3
        # 4   5    6  7
        binary_tree = BalancedBinaryTree()
        start_num = 1
        num_nodes = 7
        generated_node_values = [i for i in range(start_num, start_num + num_nodes)]

        for node_value in generated_node_values:
            binary_tree.insert_balanced(node_value)

        # Act
        # binary_tree.print_balanced_in_order()
        balanced_tree_nodes = binary_tree.traverse_balanced_in_order()
        balanced_tree_values = [node.value for node in balanced_tree_nodes]

        # Assert
        expected_node_values = generated_node_values
        self.assertListEqual(expected_node_values, balanced_tree_values)
