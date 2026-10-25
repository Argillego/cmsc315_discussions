## Implementation Summary

I implemented the four list operations in `unit3_lists.py`:

- **insert_at**: I used `list.insert()`, which shifts all elements at or
  beyond the target index one position right. I documented that insertion
  at the end is O(1) while beginning/middle insertions are O(n), and I
  validated the index (0 through len) to safely support appending.

- **delete_at**: I used `list.pop()` with prior index validation. Invalid
  indices return `None` instead of raising `IndexError`, making the
  function safe to compose into larger programs. Elements after the
  removed position shift left to close the gap.

- **search_value**: I implemented a linear search that scans sequentially
  from index 0, returning the first matching index or -1. I explained why
  a Python list requires linear search: it offers positional access only,
  with no keyed lookup, so value lookup is O(n) worst case.

- **main / tests**: I demonstrated insertion, deletion, and search at the
  beginning, middle, and end, printing the list before and after each
  operation so the element-shifting behavior is visible in the output.

- **Edge cases**: I demonstrated four — deleting at an out-of-range index,
  searching an empty list, inserting into an empty list, and deleting from
  an empty list. All returned safely (None or -1) without exceptions.