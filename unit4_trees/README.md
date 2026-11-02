# Unit 4 Discussion: Binary Search Trees

## Overview

I completed the starter Python program by implementing a Binary Search
Tree (BST) with recursive insertion, recursive search, and in-order
traversal. I kept the original TODO prompts in the code and added
comments explaining each operation.

## What I implemented

I built the tree with a `Node` class that stores a value and two child
references, `left` and `right`, both initialized to `None`. The `BST`
class starts with `root = None`, so a new tree begins empty.

I implemented `insert()` using a recursive helper,
`_insert_recursive()`. The insertion logic depends on comparisons
because the BST property requires smaller values to live in the left
subtree and larger values in the right subtree. When the recursion
reaches an empty position (`None`), it creates a new node there.
Equal values are ignored, so the tree never stores duplicates. Each
call returns the updated node reference so parent links stay intact.

I implemented `search()` using `_search_recursive()`, which compares
the target to the current node and descends only one branch — left for
smaller targets, right for larger ones — until it finds a match or
reaches an empty spot and returns `False`.

I implemented `inorder()` using `_inorder_recursive()`, which visits
the left subtree first, then the current node, then the right subtree.
The traversal returns the collected values as a list.

### Demonstration in main()

I inserted the values `[50, 30, 70, 20, 40, 60, 80]`, starting with the
middle value 50 so the tree stays balanced. Each insertion descends a
single path, cutting the search space roughly in half at every step.
The in-order traversal printed `[20, 30, 40, 50, 60, 70, 80]`, sorted
with no extra sorting step. Searches for 40 and 80 returned `True`;
searches for 35 and 90 returned `False` because the search fell off
the edge of the tree.

### Edge cases

I demonstrated three edge cases:

- **Empty tree:** searching an empty tree returned `False` and
  traversing it returned `[]`, because the recursive base case stops
  immediately on a `None` node.
- **Duplicate insertion:** inserting 50 again left the tree unchanged,
  since `_insert_recursive()` takes neither the left nor right branch
  on equal values.
- **Single-node tree:** a tree with only the root returned `[42]` from
  traversal and `True` from searching for that value.

## Performance

Each node stores one value and two references, so memory usage grows
proportionally to the number of values, or O(n). Insertion and search
follow a single path from the root, so for a balanced tree they take
O(log n), because every comparison eliminates an entire subtree — much
faster than the O(n) of a linear search through a list. The in-order
traversal always visits every node once, so it is O(n). In the worst
case, inserting already-sorted data degrades the tree into a linked
list, which returns operations to O(n).

## Real-world use

A file system's directory structure is a real-world tree example:
folders branch into subfolders the way nodes branch into children, and
a search descends one branch at a time instead of scanning every file.
Contact lists and dictionaries work the same way — alphabetical
ordering lets each comparison discard half of the remaining entries.

## Running the program

I ran the completed program with:

    python unit4_trees.py

The program printed the inserted values, the sorted in-order traversal,
the search results, and the edge case demonstrations, finishing with
exit code 0.

## Reflection

This assignment helped me understand that a BST's efficiency comes
entirely from its ordering rule. The main challenge I worked through
was the recursive insertion pattern: each call returns the updated
node so the parent keeps a valid link, and tracing a single insert on
paper made that click. Comparing the BST to linear structures showed
me why ordering matters — a balanced BST finds a value in about
log2(n) comparisons, while a linear search of an array or linked list
checks every element one by one. I also learned that in-order
traversal produces sorted output for free: the structure itself does
the sorting. The trade-off is balance — sequential input turns the
BST into a linked list, which is why self-balancing trees like AVL
and Red-Black trees rotate nodes to keep the height logarithmic.