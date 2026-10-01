"""Graph algorithms over adjacency dictionaries.

Graph format::

    graph = {
        "a": [("b", 2), ("c", 1)],   # (neighbour, weight)
        "b": [],
        "c": [],
    }
"""

from __future__ import annotations

import heapq
from collections import deque
from typing import Any

Graph = dict[Any, list[tuple[Any, float]]]


def bfs(graph: Graph, start: Any) -> list[Any]:
    """Breadth-first traversal order starting from ``start``."""
    visited = {start}
    order: list[Any] = []
    queue: deque[Any] = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour, _weight in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order


def dfs(graph: Graph, start: Any) -> list[Any]:
    """Depth-first traversal order (iterative)."""
    visited: set[Any] = set()
    order: list[Any] = []
    stack: list[Any] = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbour, _weight in reversed(graph.get(node, [])):
            if neighbour not in visited:
                stack.append(neighbour)
    return order


def dijkstra(graph: Graph, start: Any) -> dict[Any, float]:
    """Shortest distances from ``start`` (non-negative weights)."""
    distances: dict[Any, float] = {start: 0.0}
    heap: list[tuple[float, Any]] = [(0.0, start)]

    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances.get(node, float("inf")):
            continue
        for neighbour, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbour, float("inf")):
                distances[neighbour] = candidate
                heapq.heappush(heap, (candidate, neighbour))
    return distances


def topological_sort(graph: Graph) -> list[Any]:
    """Kahn's algorithm; raises ValueError when the graph has a cycle."""
    in_degree: dict[Any, int] = {node: 0 for node in graph}
    for node in graph:
        for neighbour, _weight in graph[node]:
            in_degree[neighbour] = in_degree.get(neighbour, 0) + 1

    queue: deque[Any] = deque(node for node, degree in in_degree.items() if degree == 0)
    order: list[Any] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour, _weight in graph.get(node, []):
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(order) != len(in_degree):
        raise ValueError("graph contains a cycle")
    return order


def has_cycle(graph: Graph) -> bool:
    """True when the directed graph contains a cycle."""
    try:
        topological_sort(graph)
        return False
    except ValueError:
        return True
