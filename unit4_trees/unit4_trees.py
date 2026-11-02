"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value      # the data this node holds
        self.left = None        # reference to the left child (smaller values)
        self.right = None       # reference to the right child (larger values)


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None        # an empty tree has no root node

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion depends on comparisons because the BST property
        # requires every value to be ordered: smaller values must
        # live in the left subtree and larger values in the right
        # subtree. Following the correct branch keeps the tree
        # organized so future searches can skip half the tree at
        # each step.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: an empty position was found, so create a new node here
        if node is None:
            return Node(value)

        # Smaller values go into the left subtree
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # Larger values go into the right subtree
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Equal values are ignored, which prevents duplicates

        # Return the updated node reference so the parent keeps its link
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is more efficient than linear search because each
        # comparison eliminates an entire subtree. A linear search
        # checks every element one by one (O(n)), while a balanced BST
        # search halves the remaining search space at every step
        # (O(log n)).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case: reached an empty spot, so the value is not in the tree
        if node is None:
            return False

        # Base case: current node matches the target
        if value == node.value:
            return True

        # Recursive case: go left if target is smaller, right if larger
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []                     # collect the visited values
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # This traversal produces sorted output because of the BST
        # property: everything in the left subtree is smaller than the
        # current node, and everything in the right subtree is larger.
        # Visiting left -> current -> right therefore emits each value
        # exactly in ascending order.

        # Base case: an empty subtree (None node) has nothing to visit
        if node is None:
            return

        # Visit the left subtree first (all smaller values)
        self._inorder_recursive(node.left, values)

        # Visit the current node
        values.append(node.value)

        # Visit the right subtree last (all larger values)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create a BST object
    tree = BST()

    # Insert 7 values. Starting with 50 (the middle value) keeps the
    # tree balanced. A BST is efficient because every insertion
    # compares against a node and descends only ONE branch, cutting
    # the remaining search space roughly in half at each step. For
    # example, inserting 30 skips the entire right subtree of 50.
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    # Insert each value into the tree
    for value in values_to_insert:
        tree.insert(value)

    # Display the values inserted
    print("Values inserted:", values_to_insert)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # Perform an in-order traversal and display the results
    result = tree.inorder()
    print("In-order traversal:", result)

    # The traversal produces sorted output because of the BST
    # property: all values in a node's left subtree are smaller than
    # the node, and all values in its right subtree are larger.
    # Visiting left -> node -> right therefore emits values in
    # ascending order without any extra sorting step.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Search for two values that exist in the tree.
    # Each search only follows one path down the tree, so it makes
    # at most about log2(7) = 3 comparisons instead of scanning
    # all 7 values like a linear search would.
    print("Search 40 (exists):", tree.search(40))    # True
    print("Search 80 (exists):", tree.search(80))    # True

    # Search for two values that do not exist. The search falls off
    # the edge of the tree (reaches a None child) and returns False.
    print("Search 35 (missing):", tree.search(35))   # False
    print("Search 90 (missing):", tree.search(90))   # False

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: search and traverse an EMPTY tree.
    # Both operations handle the root being None gracefully:
    # the search returns False and the traversal returns an
    # empty list, because the recursive base case stops
    # immediately on a None node.
    empty_tree = BST()
    print("Search in empty tree:", empty_tree.search(50))    # False
    print("Traverse empty tree:", empty_tree.inorder())      # []

    # Edge case 2: inserting a DUPLICATE value.
    # My _insert_recursive ignores values that already exist
    # (neither the left nor the right branch is taken), so the
    # tree is unchanged and no duplicate node is created.
    tree.insert(50)   # 50 already exists
    print("After inserting duplicate 50:", tree.inorder())   # still sorted, no duplicate

    # Edge case 3: a tree with only ONE node.
    # The root itself is both the start and end of every search
    # path; traversal returns just that single value.
    single = BST()
    single.insert(42)
    print("Single-node traversal:", single.inorder())        # [42]
    print("Single-node search 42:", single.search(42))       # True


if __name__ == "__main__":
    main()
