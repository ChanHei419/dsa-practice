"""Binary search variants on sorted sequences."""

from __future__ import annotations

from typing import Any


def binary_search(items: list[Any], target: Any) -> int:
    """Return the index of ``target``, or -1 when absent. O(log n)."""
    low, high = 0, len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def lower_bound(items: list[Any], target: Any) -> int:
    """First index whose value is >= target (len(items) if none)."""
    low, high = 0, len(items)
    while low < high:
        middle = (low + high) // 2
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle
    return low


def upper_bound(items: list[Any], target: Any) -> int:
    """First index whose value is > target (len(items) if none)."""
    low, high = 0, len(items)
    while low < high:
        middle = (low + high) // 2
        if items[middle] <= target:
            low = middle + 1
        else:
            high = middle
    return low


def count_occurrences(items: list[Any], target: Any) -> int:
    """Number of times target appears in a sorted list. O(log n)."""
    return upper_bound(items, target) - lower_bound(items, target)
