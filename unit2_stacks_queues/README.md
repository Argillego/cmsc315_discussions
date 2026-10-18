# Unit 2 Discussion: Stacks and Queues

## Overview

This project implements two fundamental linear data structures in Python: a **stack** (LIFO) and a **queue** (FIFO). The program defines a `Stack` class and a `Queue` class, demonstrates each structure's ordering behavior with clear output, and tests edge cases such as removing from or viewing an empty structure.

## Implementation Summary

- **Stack class:** I implemented the stack using a Python list, since `append()` and `pop()` both operate on the end of the list in O(1) time. `push()` adds to the end and `pop()` removes from the end, so the newest value is always removed first — the LIFO behavior. `peek()` returns the top value without removing it, and `is_empty()` reports whether the stack has any values.

- **Queue class:** I implemented the queue using `collections.deque`, which provides O(1) operations at both ends (using a plain list's `pop(0)` would be O(n)). `enqueue()` adds to the back and `dequeue()` removes from the front, so the oldest value always leaves first — the FIFO behavior. `front()` returns the front value without removing it, and `is_empty()` reports whether the queue has any values.

- **LIFO demonstration:** I pushed four tasks onto the stack and popped two. The output showed `task4` (the last one pushed) came off first, followed by `task3`, confirming last-in, first-out ordering.

- **FIFO demonstration:** I enqueued four customers and dequeued two. The output showed `customerA` (the first one enqueued) left first, followed by `customerB`, confirming first-in, first-out ordering.

- **Edge cases:** I tested removing and viewing from empty structures — both returned a friendly message instead of raising an `IndexError`, because `pop()`, `peek()`, `dequeue()`, and `front()` all check `is_empty()` first. I also created single-item stack and queue instances, removed the only item, and verified both structures reported empty afterward.

## Why LIFO and Why FIFO

A stack uses LIFO because its use cases naturally reverse order: an undo history replays the most recent change first, and a browser's back button returns to the most recently visited page. A queue uses FIFO because its use cases are fair, first-come-first-served systems: a print queue serves documents in submission order, and a customer service line serves whoever has waited longest.

## Memory Usage

Both structures grow linearly, O(n): each pushed or enqueued value adds exactly one slot to memory, and removing a value frees that slot. Neither structure stores extra copies or overhead per item, so memory usage is directly proportional to the number of values currently held.

## How to Run

Run the file with Python 3:
