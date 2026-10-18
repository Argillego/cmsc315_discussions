"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

A stack removes its most recently added item first (LIFO),
while a queue removes its oldest item first (FIFO). This
program implements both, demonstrates their ordering
behavior, and tests edge cases on empty structures.
"""

from collections import deque


class Stack:
    """A stack (LIFO): the last value pushed is the first popped."""

    def __init__(self):
        # A Python list works well as a stack because append() and
        # pop() both operate on the END of the list, which is O(1).
        self._items = []

    def push(self, value):
        # push() adds to the end of the list. Because removal also
        # happens at the end, the newest value is always removed
        # first -- this is exactly what makes the stack LIFO.
        self._items.append(value)

    def pop(self):
        # pop() removes and returns the LAST appended value.
        # Edge case: popping an empty list raises IndexError, so we
        # check first and return a message instead of crashing.
        if self.is_empty():
            return "Cannot pop: the stack is empty."
        return self._items.pop()

    def peek(self):
        # peek() returns the top (last) value WITHOUT removing it,
        # so the stack is unchanged after the call.
        if self.is_empty():
            return "Cannot peek: the stack is empty."
        return self._items[-1]

    def is_empty(self):
        # True when there are no values left in the stack.
        return len(self._items) == 0


class Queue:
    """A queue (FIFO): the first value enqueued is the first dequeued."""

    def __init__(self):
        # collections.deque gives O(1) operations at BOTH ends,
        # which is ideal for a queue (list.pop(0) would be O(n)).
        self._items = deque()

    def enqueue(self, value):
        # enqueue() adds to the BACK (right end). Removal happens
        # at the FRONT, so the oldest value always leaves first --
        # this is what makes the queue FIFO.
        self._items.append(value)

    def dequeue(self):
        # dequeue() removes and returns the value at the FRONT,
        # i.e., the value that has been waiting the longest.
        # Edge case: we return a message instead of crashing when
        # the queue is empty.
        if self.is_empty():
            return "Cannot dequeue: the queue is empty."
        return self._items.popleft()

    def front(self):
        # front() returns the value at the front of the queue
        # WITHOUT removing it, so the queue is unchanged.
        if self.is_empty():
            return "Cannot view front: the queue is empty."
        return self._items[0]

    def is_empty(self):
        # True when there are no values left in the queue.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO (LIFO) ===")

    # 1. Create a Stack object.
    stack = Stack()

    # 2-3. Add values with clear, explanatory output.
    print("Pushing: 'task1', 'task2', 'task3', 'task4'")
    stack.push("task1")
    stack.push("task2")
    stack.push("task3")
    stack.push("task4")

    # 4. Demonstrate LIFO: the LAST value pushed comes off FIRST.
    print("Popped:", stack.pop(), "(last one in came out first -> LIFO)")
    print("Popped:", stack.pop(), "(next newest comes out next)")
    print("Top of stack now (peek):", stack.peek())

    # 5. Empty the stack, then pop again to show the edge case.
    stack.pop()
    stack.pop()
    print("Stack is empty:", stack.is_empty())
    print("Pop on empty stack:", stack.pop())

    # 6. Peek on an empty stack.
    print("Peek on empty stack:", stack.peek())

    # 7. Single-item stack: remove it and verify the stack is empty.
    single = Stack()
    single.push("only item")
    print("Removed:", single.pop())
    print("Single-item stack empty after removal:", single.is_empty())

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO (FIFO) ===")

    # 1. Create a Queue object.
    queue = Queue()

    # 2-3. Add values with clear, explanatory output.
    print("Enqueuing: 'customerA', 'customerB', 'customerC', 'customerD'")
    queue.enqueue("customerA")
    queue.enqueue("customerB")
    queue.enqueue("customerC")
    queue.enqueue("customerD")

    # 4. Demonstrate FIFO: the FIRST value enqueued leaves FIRST.
    print("Dequeued:", queue.dequeue(), "(first one in came out first -> FIFO)")
    print("Dequeued:", queue.dequeue(), "(next oldest comes out next)")
    print("Front of queue now:", queue.front())

    # 5. Empty the queue, then dequeue again to show the edge case.
    queue.dequeue()
    queue.dequeue()
    print("Queue is empty:", queue.is_empty())
    print("Dequeue on empty queue:", queue.dequeue())

    # 6. View the front of an empty queue.
    print("Front on empty queue:", queue.front())

    # 7. Single-item queue: remove it and verify the queue is empty.
    single_q = Queue()
    single_q.enqueue("only customer")
    print("Removed:", single_q.dequeue())
    print("Single-item queue empty after removal:", single_q.is_empty())


if __name__ == "__main__":
    main()