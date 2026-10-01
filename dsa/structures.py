"""Classic data structures implemented from scratch."""

from __future__ import annotations

from collections import deque
from typing import Any, Iterator


class Stack:
    """LIFO stack backed by a Python list."""

    def __init__(self) -> None:
        self._items: list[Any] = []

    def push(self, value: Any) -> None:
        self._items.append(value)

    def pop(self) -> Any:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class Queue:
    """FIFO queue backed by collections.deque."""

    def __init__(self) -> None:
        self._items: deque[Any] = deque()

    def enqueue(self, value: Any) -> None:
        self._items.append(value)

    def dequeue(self) -> Any:
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class _Node:
    __slots__ = ("value", "next")

    def __init__(self, value: Any, next_node: "_Node | None" = None) -> None:
        self.value = value
        self.next = next_node


class LinkedList:
    """Singly linked list with append, prepend, remove, and iteration."""

    def __init__(self) -> None:
        self.head: _Node | None = None
        self._length = 0

    def append(self, value: Any) -> None:
        node = _Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self._length += 1

    def prepend(self, value: Any) -> None:
        self.head = _Node(value, self.head)
        self._length += 1

    def remove(self, value: Any) -> bool:
        previous: _Node | None = None
        current = self.head
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self._length -= 1
                return True
            previous, current = current, current.next
        return False

    def to_list(self) -> list[Any]:
        return list(self)

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._length


class MinHeap:
    """Binary min-heap with O(log n) push and pop."""

    def __init__(self) -> None:
        self._items: list[Any] = []

    def push(self, value: Any) -> None:
        self._items.append(value)
        self._sift_up(len(self._items) - 1)

    def pop(self) -> Any:
        if not self._items:
            raise IndexError("pop from empty heap")
        smallest = self._items[0]
        last = self._items.pop()
        if self._items:
            self._items[0] = last
            self._sift_down(0)
        return smallest

    def peek(self) -> Any:
        if not self._items:
            raise IndexError("peek from empty heap")
        return self._items[0]

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self._items[index] < self._items[parent]:
                self._items[index], self._items[parent] = (
                    self._items[parent],
                    self._items[index],
                )
                index = parent
            else:
                break

    def _sift_down(self, index: int) -> None:
        size = len(self._items)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < size and self._items[left] < self._items[smallest]:
                smallest = left
            if right < size and self._items[right] < self._items[smallest]:
                smallest = right
            if smallest == index:
                break
            self._items[index], self._items[smallest] = (
                self._items[smallest],
                self._items[index],
            )
            index = smallest

    def __len__(self) -> int:
        return len(self._items)


class UnionFind:
    """Disjoint-set forest with path compression and union by rank."""

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)
