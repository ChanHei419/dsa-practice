"""Sorting algorithms with average/worst-case complexity notes."""

from __future__ import annotations

from typing import Any


def insertion_sort(items: list[Any]) -> list[Any]:
    """O(n^2) worst case, O(n) on nearly-sorted input. Stable."""
    result = list(items)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result


def merge_sort(items: list[Any]) -> list[Any]:
    """O(n log n) time, O(n) space. Stable."""
    if len(items) <= 1:
        return list(items)

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    merged: list[Any] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(items: list[Any]) -> list[Any]:
    """O(n log n) average, O(n^2) worst case. Lomuto partition, not stable."""
    result = list(items)
    _quick_sort_range(result, 0, len(result) - 1)
    return result


def _quick_sort_range(items: list[Any], low: int, high: int) -> None:
    if low >= high:
        return
    pivot_index = _partition(items, low, high)
    _quick_sort_range(items, low, pivot_index - 1)
    _quick_sort_range(items, pivot_index + 1, high)


def _partition(items: list[Any], low: int, high: int) -> int:
    pivot = items[high]
    boundary = low
    for index in range(low, high):
        if items[index] <= pivot:
            items[boundary], items[index] = items[index], items[boundary]
            boundary += 1
    items[boundary], items[high] = items[high], items[boundary]
    return boundary


def heap_sort(items: list[Any]) -> list[Any]:
    """O(n log n) time, O(1) extra space. Not stable."""
    result = list(items)
    size = len(result)

    for start in range(size // 2 - 1, -1, -1):
        _sift_down(result, start, size)

    for end in range(size - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        _sift_down(result, 0, end)

    return result


def _sift_down(items: list[Any], root: int, size: int) -> None:
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < size and items[left] > items[largest]:
            largest = left
        if right < size and items[right] > items[largest]:
            largest = right
        if largest == root:
            break
        items[root], items[largest] = items[largest], items[root]
        root = largest
