"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Search the list from beginning to end, one element at a time.
    for i in range(len(lst)):
        # Compare the current element against the target.
        if lst[i] == target:
            return i  # Return the index if the target is found.

    # Why O(n): in the worst case (target absent or at the end),
    # every one of the n elements must be examined once. The work
    # grows in direct proportion to the list size, so doubling the
    # list doubles the maximum number of comparisons -> O(n).
    return -1  # Return -1 if the target is not found.


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    # Keep searching while the range still contains candidates.
    while high >= low:
        # Middle index of the current search space
        # (integer division for a valid list index).
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid  # Return the index if the target is found.
        elif lst[mid] < target:
            # Target must be in the RIGHT half: discard everything
            # at mid and to the left of it.
            low = mid + 1
        else:
            # Target must be in the LEFT half: discard everything
            # at mid and to the right of it.
            high = mid - 1

        # How each iteration reduces the search space: every single
        # comparison eliminates the middle element AND one entire
        # half of the remaining range. A range of n becomes roughly
        # n/2, then n/4, then n/8 ... so after k comparisons only
        # n / 2^k candidates remain. This halving is why binary
        # search is O(log n): for 1,024 elements at most ~11
        # comparisons are ever needed.

    return -1  # Return -1 if the target is not found.


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # 1. A small sorted dataset of student scores.
    small_dataset = [55, 67, 72, 81, 90, 95]

    # 2-3. Search for a value that EXISTS (81, at index 3) and one
    # that DOES NOT exist (75).
    existing = 81
    missing = 75

    print(f"Dataset: {small_dataset}")

    result = linear_search(small_dataset, existing)
    print(f"Linear search for {existing}: index {result}"
          f"  (found after {result + 1} comparisons)")

    result = binary_search(small_dataset, existing)
    print(f"Binary search for {existing}: index {result}"
          f"  (midpoints checked: 72, then 81 -> 2 comparisons)")

    result = linear_search(small_dataset, missing)
    print(f"Linear search for {missing}: index {result}"
          f"  (-1 because all 6 elements were checked)")

    result = binary_search(small_dataset, missing)
    print(f"Binary search for {missing}: index {result}"
          f"  (-1 after only ~3 comparisons because the"
          f" search space halved each step)")

    # 4. Explanation: on this tiny dataset both algorithms are fast,
    # but linear search already did more work (up to 6 checks vs 2-3),
    # foreshadowing the gap that opens up on large datasets.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # 1. A much larger sorted dataset: 1,024 elements.
    large_dataset = list(range(0, 2048, 2))  # [0, 2, 4, ..., 2046]

    # 2. Search for a value near the end so linear search does
    # nearly its maximum amount of work.
    target = 2044

    linear_result = linear_search(large_dataset, target)
    binary_result = binary_search(large_dataset, target)

    # 3. Compare the results.
    print(f"Dataset size: {len(large_dataset)} sorted elements")
    print(f"Linear search for {target}: index {linear_result}"
          f"  ({linear_result + 1} comparisons)")
    print(f"Binary search for {target}: index {binary_result}"
          f"  (at most {len(large_dataset).bit_length()} comparisons)")

    # Explicit comparison of observed performance for clarity.
    print(f"\nComparison: linear search needed {linear_result + 1}"
          f" comparisons while binary search needed at most"
          f" {len(large_dataset).bit_length()} for the same target."
          " Each binary search comparison discarded half of the"
          " remaining candidates, while linear search examined"
          " elements one by one -- this is O(log n) vs O(n).")

    # 4. Why binary search scales better: linear search performed
    # 1,023 comparisons here because work grows as O(n). Binary
    # search found the same element in about 10 comparisons because
    # each step halves the search space (O(log n)). Doubling the
    # dataset doubles linear search's worst case but adds only ONE
    # extra comparison for binary search.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: EMPTY LIST. high starts at -1, so the binary
    # search loop never runs; both methods return -1 with zero
    # comparisons instead of crashing.
    empty = []
    print(f"Empty list | linear: {linear_search(empty, 5)}"
          f" | binary: {binary_search(empty, 5)}"
          f"  (both return -1 safely, no comparisons)")

    # Edge case 2: SINGLE-ELEMENT LIST. The list has exactly one
    # candidate; found -> index 0, not found -> -1.
    single = [42]
    print(f"Single-element list | find 42: linear {linear_search(single, 42)}"
          f", binary {binary_search(single, 42)}"
          f"  (found at index 0)")
    print(f"Single-element list | find 7: linear {linear_search(single, 7)}"
          f", binary {binary_search(single, 7)}"
          f"  (both return -1)")

    # Edge case 3: FIRST AND LAST POSITIONS. Targets at the exact
    # boundaries of the list must still be found correctly --
    # this catches off-by-one errors in low/high updates.
    first_last = [10, 20, 30, 40, 50]
    print(f"First element (10): linear {linear_search(first_last, 10)}"
          f", binary {binary_search(first_last, 10)}"
          f"  (boundary index 0)")
    print(f"Last element (50): linear {linear_search(first_last, 50)}"
          f", binary {binary_search(first_last, 50)}"
          f"  (boundary index 4)")

    # Edge case 4: VALUE NOT PRESENT (between existing values).
    # 35 falls between 30 and 40; both searches exhaust the space
    # and correctly return -1 rather than returning a wrong index.
    print(f"Missing mid value (35): linear {linear_search(first_last, 35)}"
          f", binary {binary_search(first_last, 35)}"
          f"  (both return -1)")


if __name__ == "__main__":
    main()