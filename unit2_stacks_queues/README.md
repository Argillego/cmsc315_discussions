# Unit 2 Discussion: Stacks and Queues

## Overview

This project implements two fundamental linear data structures in Python: a **stack** (LIFO) and a **queue** (FIFO). The program defines a `Stack` class and a `Queue` class, demonstrates each structure's ordering behavior with clearly labeled output, tests edge cases on empty structures, and ends with a real-world scenario comparing a coffee shop line (queue) with a text editor's undo history (stack).

## Implementation Summary

- **Stack class:** I implemented the stack using a Python list, since `append()` and `pop()` both operate on the end of the list in O(1) time. `push()` adds to the end and `pop()` removes from the end, so the newest value is always removed first — the LIFO behavior. `peek()` returns the top value without removing it, and `is_empty()` reports whether the stack has any values.

- **Queue class:** I implemented the queue using `collections.deque`, which provides O(1) operations at both ends (using a plain list's `pop(0)` would be O(n)). `enqueue()` adds to the back and `dequeue()` removes from the front, so the oldest value always leaves first — the FIFO behavior. `front()` returns the front value without removing it, and `is_empty()` reports whether the queue has any values.

- **LIFO demonstration:** I pushed four tasks onto the stack and popped two. The output showed `task4` (the last one pushed) came off first, followed by `task3`, confirming last-in, first-out ordering.

- **FIFO demonstration:** I enqueued four customers and dequeued two. The output showed `customerA` (the first one enqueued) left first, followed by `customerB`, confirming first-in, first-out ordering.

- **Edge cases:** I tested removing and viewing from empty structures — both returned a friendly message instead of raising an `IndexError`, because `pop()`, `peek()`, `dequeue()`, and `front()` all check `is_empty()` first. I also created single-item stack and queue instances, removed the only item, and verified both structures reported empty afterward.

- **Real-world scenario:** I simulated a coffee shop line as a queue — Dana, Marcus, Priya, and Elena join in order, and Dana (the first to arrive) is served first, demonstrating FIFO fairness. I also simulated a text editor's undo history as a stack — the user types, deletes, and pastes, and pressing Ctrl+Z undoes the paste (the most recent action) first, demonstrating LIFO recency.

## Why a Stack Uses LIFO and a Queue Uses FIFO

A stack uses LIFO because its most natural applications reverse order: an undo feature in a text editor must undo the *most recent* change first, and a browser's back button must return to the *most recently* visited page. The newest item is always the one needed next, so removal happens at the same end where addition happens.

A queue uses FIFO because its applications are fairness systems: a print queue processes documents in the order they were submitted, and a customer service line serves whoever has waited longest. The oldest item must leave first, so removal happens at the opposite end from addition.

## Memory Usage

Both structures grow linearly — O(n) memory. Each `push()` or `enqueue()` adds exactly one slot, each removal frees one slot, and neither structure stores extra per-item overhead. Memory usage is directly proportional to the number of values currently held, unlike fixed-size array implementations that may reserve unused capacity.

## How to Run

Run the file with Python 3:

    python unit2_discussion.py

The output walks through the stack demo (LIFO), the queue demo (FIFO), the edge-case tests, and the real-world scenario.

## Reflection

Completing this assignment taught me how ordering rules define data structures: the same add/remove operations produce completely different behavior depending on which end you remove from. I learned why implementation choice matters — I used `collections.deque` for the queue because removing from the front of a plain list shifts every element, turning an O(1) operation into O(n). The biggest challenge was designing edge-case handling: my first instinct was to let Python raise an `IndexError` on an empty structure, but a real application should return a clear message instead, so I added `is_empty()` checks before every removal and peek. In real-world terms, stacks and queues differ in recency versus fairness: stacks power undo histories, browser back buttons, and the function call stack, while queues power print spoolers, customer service lines, and task schedulers where first-come, first-served is the requirement. Choosing between them is really choosing whether "next" means the newest item or the oldest one.