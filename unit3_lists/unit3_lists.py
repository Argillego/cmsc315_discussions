"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    Implementation: Python's list.insert(index, value) does the work.
    After an insertion occurs, every element that sits at or beyond the
    target index is shifted one position to the right (toward the end)
    to make room, and the list's length grows by one. Elements before
    the index are untouched.

    Performance: inserting at the END (index == len(lst)) is O(1) because
    no elements need to move. Inserting at the BEGINNING (index 0) is the
    worst case, O(n), because every single element must shift right one
    slot. A MIDDLE insertion is O(n) as well, since on average n/2
    elements shift. Python lists are backed by a contiguous array of
    references, so shifting is a fast memmove-style operation, but the
    cost still grows with list size.
    """
    # Validate the index: allow 0 up to and including len(lst),
    # since inserting exactly at the end is legal (it appends).
    if index < 0 or index > len(lst):
        # Silently ignore invalid positions rather than crash;
        # alternatively an exception could be raised.
        return lst
    lst.insert(index, value)  # shifts later elements right automatically
    return lst


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    Implementation: list.pop(index) removes the element and returns it.
    After deletion, every element after the removed position shifts one
    position LEFT to close the gap, and the length shrinks by one.

    Why validation matters: an unvalidated index raises IndexError
    (e.g., deleting from an empty list, or index >= len(lst)). Validating
    first and returning None on an invalid index makes the function safe
    to call in loops or pipelines where a crash would break the whole
    program — "safe deletion" means the caller can always handle the
    result without try/except boilerplate.
    """
    # Index must point at an existing element: 0 .. len(lst)-1.
    if index < 0 or index >= len(lst):
        return None  # invalid index: nothing to remove
    return lst.pop(index)  # shifts later elements left automatically


def search_value(lst, value):
    """
    Search for a value within the list.

    Returns the index if found, -1 if not.

    Why this is a linear search: Python lists only support direct access
    by index (lst[i]), not by value. To locate a value we must compare
    candidate elements one at a time, scanning sequentially from index 0
    to the end. There is no way to "jump" to a value the way a hash table
    or balanced search tree can, because the list is not sorted or keyed.
    Worst case is O(n) (value missing or at the end); best case O(1)
    (value at index 0). Note: Python's built-in `in` operator and
    list.index() perform the same kind of sequential scan internally.
    """
    # Linear scan: check each position in order.
    for i in range(len(lst)):
        if lst[i] == value:
            return i  # found: return position of first match
    return -1  # scanned the whole list without a match


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    # Step 1: create a list with several values to work with.
    songs = ["Song A", "Song B", "Song C", "Song D"]
    print("Original list:", songs)

    # Step 2: insert at the BEGINNING (index 0).
    # Worst case: every existing element shifts right one slot -> O(n).
    insert_at(songs, 0, "Intro")
    print("After inserting 'Intro' at index 0 (beginning):", songs)

    # Step 3: insert in the MIDDLE (index 2).
    # Roughly half the elements shift -> still O(n) on average.
    insert_at(songs, 2, "Interlude")
    print("After inserting 'Interlude' at index 2 (middle):", songs)

    # Step 4: insert at the END (index == len(lst)).
    # Best case: nothing after it, no shifting required -> O(1).
    insert_at(songs, len(songs), "Outro")
    print("After inserting 'Outro' at the end:", songs)

    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")

    # Delete from the BEGINNING: all remaining elements shift left -> O(n).
    removed = delete_at(songs, 0)
    print(f"Removed from beginning: {removed} -> list is now {songs}")

    # Delete from the MIDDLE: only elements after it shift left -> O(n).
    removed = delete_at(songs, 2)
    print(f"Removed from middle (index 2): {removed} -> list is now {songs}")

    # Delete from the END: no shifting needed -> O(1).
    removed = delete_at(songs, len(songs) - 1)
    print(f"Removed from end: {removed} -> list is now {songs}")

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Search for a value that EXISTS: linear scan finds it, returns index.
    result = search_value(songs, "Song B")
    print(f"Searching for 'Song B': found at index {result}")

    # Search for a value that does NOT exist: full scan, returns -1.
    result = search_value(songs, "Song Z")
    print(f"Searching for 'Song Z' (missing): result {result} (-1 means not found)")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge case 1: delete using an INVALID index (out of range).
    # delete_at validates first and returns None instead of raising
    # IndexError, so the program keeps running.
    result = delete_at(songs, 100)
    print(f"Deleting at index 100 (invalid): returned {result} -> list unchanged: {songs}")

    # Edge case 2: search an EMPTY list for a value.
    # The loop body never executes, so it correctly returns -1.
    empty_list = []
    result = search_value(empty_list, "Song A")
    print(f"Searching an empty list: returned {result} (-1, no crash)")

    # Edge case 3: insert into an EMPTY list at index 0.
    # index 0 == len(empty_list) == 0, so this is legal and appends.
    insert_at(empty_list, 0, "First Song")
    print(f"After inserting into an empty list: {empty_list}")

    # Edge case 4: delete from an EMPTY list.
    # Validation catches it: len == 0, so no index is valid -> None.
    result = delete_at(empty_list, 0)
    print(f"Deleting from an empty list: returned {result} (None, no crash)")


if __name__ == "__main__":
    main()