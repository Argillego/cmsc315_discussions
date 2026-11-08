# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. **Test both algorithms on a small dataset.** I tested both search
   methods on a sorted list of 6 student scores and confirmed that each
   method returned the correct index for the target score. Linear search
   found the existing target after 4 comparisons and binary search found
   it after only 2; both correctly returned -1 for a missing value.

2. **Test both algorithms on a large dataset.** I tested both methods on
   a sorted list of 1,024 scores. Linear search needed 1,023 comparisons
   to find the target near the end of the list, while binary search
   located it in about 10 comparisons -- and would never need more
   than 11 regardless of target.

3. **Demonstrate edge cases.** I verified that both methods returned -1
   when the target was not present, and that binary search handled an
   empty list safely by returning -1 without executing any comparisons.
   I also tested a single-element list, targets at the first and last
   positions, and a missing value falling between two existing values.

4. **Analyze performance.** Linear search grew linearly with the number
   of elements, O(N), because it examined each element in sequence.
   Binary search eliminated half of the remaining candidates on every
   comparison, O(log N), so doubling the dataset added only one
   additional comparison. On the 1,024-element dataset this amounted to
   1,023 comparisons for linear search versus roughly 10 for binary
   search on the same target.

5. **Create a real-world search scenario.** I modeled a school
   administrator looking up a student's score in a records system:
   linear search suits a small, frequently re-ordered roster, while
   binary search suits a large, alphabetically or numerically sorted
   transcript archive where lookups must stay fast.

## How to Run

I ran the program in PyCharm by executing unit5_discussion.py. The
output displayed three sections: a small dataset test, a large dataset
comparison, and four edge case tests, with explanatory text next to
each result.

## Discussion Board Reflection

While completing this assignment, I strengthened my understanding of
search algorithm efficiency by implementing both linear and binary
search in Python and testing them on small and large datasets. I
learned that algorithm choice matters far more than implementation
details once a dataset grows large: binary search needed only about 10
comparisons on 1,024 elements where linear search needed up to 1,024.

The main challenge I encountered was managing the binary search
boundary conditions. An off-by-one error in the low and high indices
could skip elements or loop forever, and I overcame this by carefully
tracing the algorithm by hand -- writing out the midpoint indices for
small arrays until the halving pattern was clear. Handling the empty
list edge case also required care, since the initial high index had to
be set so the loop body never ran.

Linear search is the right choice when data is unsorted, small, or
changes constantly, because sorting costs would outweigh binary
search's speed advantage. Binary search is appropriate for large,
sorted, stable datasets such as dictionaries, contact lists, or
database indexes, where its O(log N) performance keeps lookups fast
at any scale.