"""
Unit 4 Discussion: Tests for the Binary Search Tree implementation.
Mirrors every class, method, and behavior in unit4_trees.py.
Run with:  python -m unittest unit4_test.py
"""

import unittest
from unit4_trees import BST, Node


class TestNode(unittest.TestCase):
    """Mirrors the Node class."""

    def test_node_stores_value(self):
        node = Node(7)
        self.assertEqual(node.value, 7)

    def test_node_children_initialized_to_none(self):
        node = Node(7)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


class TestBSTInit(unittest.TestCase):
    """Mirrors BST.__init__."""

    def test_new_tree_starts_empty(self):
        tree = BST()
        self.assertIsNone(tree.root)


class TestInsert(unittest.TestCase):
    """Mirrors insert() and _insert_recursive()."""

    def test_insert_first_value_becomes_root(self):
        tree = BST()
        tree.insert(50)
        self.assertEqual(tree.root.value, 50)

    def test_smaller_values_go_left(self):
        tree = BST()
        tree.insert(50)
        tree.insert(30)
        self.assertEqual(tree.root.left.value, 30)
        self.assertIsNone(tree.root.right)

    def test_larger_values_go_right(self):
        tree = BST()
        tree.insert(50)
        tree.insert(70)
        self.assertEqual(tree.root.right.value, 70)
        self.assertIsNone(tree.root.left)

    def test_nested_insertion(self):
        tree = BST()
        for v in [50, 30, 70, 20, 40, 60, 80]:
            tree.insert(v)
        self.assertEqual(tree.root.left.left.value, 20)
        self.assertEqual(tree.root.left.right.value, 40)
        self.assertEqual(tree.root.right.left.value, 60)
        self.assertEqual(tree.root.right.right.value, 80)

    def test_duplicate_insert_ignored(self):
        tree = BST()
        tree.insert(50)
        tree.insert(50)
        self.assertEqual(tree.inorder(), [50])
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)


class TestSearch(unittest.TestCase):
    """Mirrors search() and _search_recursive()."""

    def setUp(self):
        self.tree = BST()
        for v in [50, 30, 70, 20, 40, 60, 80]:
            self.tree.insert(v)

    def test_search_finds_root(self):
        self.assertTrue(self.tree.search(50))

    def test_search_finds_left_subtree_values(self):
        self.assertTrue(self.tree.search(30))
        self.assertTrue(self.tree.search(20))
        self.assertTrue(self.tree.search(40))

    def test_search_finds_right_subtree_values(self):
        self.assertTrue(self.tree.search(70))
        self.assertTrue(self.tree.search(60))
        self.assertTrue(self.tree.search(80))

    def test_search_missing_leaf_level_value(self):
        self.assertFalse(self.tree.search(35))

    def test_search_missing_value_beyond_tree(self):
        self.assertFalse(self.tree.search(90))

    def test_search_empty_tree_returns_false(self):
        self.assertFalse(BST().search(50))


class TestInorder(unittest.TestCase):
    """Mirrors inorder() and _inorder_recursive()."""

    def test_inorder_returns_sorted_list(self):
        tree = BST()
        for v in [50, 30, 70, 20, 40, 60, 80]:
            tree.insert(v)
        self.assertEqual(tree.inorder(), [20, 30, 40, 50, 60, 70, 80])

    def test_inorder_empty_tree_returns_empty_list(self):
        self.assertEqual(BST().inorder(), [])

    def test_inorder_single_node(self):
        tree = BST()
        tree.insert(42)
        self.assertEqual(tree.inorder(), [42])

    def test_inorder_degenerate_tree_still_sorted(self):
        tree = BST()
        for v in [1, 2, 3, 4, 5]:
            tree.insert(v)
        self.assertEqual(tree.inorder(), [1, 2, 3, 4, 5])

    def test_inorder_does_not_modify_tree(self):
        tree = BST()
        for v in [50, 30, 70]:
            tree.insert(v)
        tree.inorder()
        self.assertEqual(tree.inorder(), [30, 50, 70])


if __name__ == "__main__":
    unittest.main()
