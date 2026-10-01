# DSA Practice

![Tests](https://github.com/ChanHei419/dsa-practice/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-28%20unittest-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)

Clean, from-scratch implementations of the data structures and algorithms I use most — with complexity notes and a full test suite.

Written to stay sharp on the fundamentals from **CSCI2100 (Data Structures)** and to have a reference I can actually read.

---

## Contents

| Module | Topic | Implementations |
| --- | --- | --- |
| [`dsa/structures.py`](dsa/structures.py) | Data structures | Stack, Queue, Singly Linked List, Binary Min-Heap, Union-Find |
| [`dsa/sorting.py`](dsa/sorting.py) | Sorting | Insertion, Merge, Quick (Lomuto), Heap sort |
| [`dsa/searching.py`](dsa/searching.py) | Searching | Binary search, lower bound, upper bound |
| [`dsa/graphs.py`](dsa/graphs.py) | Graphs | BFS, DFS, Dijkstra, Kahn topological sort, cycle detection |

### Complexity cheat sheet

| Structure / Algorithm | Time | Space |
| --- | --- | --- |
| Stack / Queue | O(1) push/pop | O(n) |
| Linked list append | O(n) | O(n) |
| Binary heap push/pop | O(log n) | O(n) |
| Union-Find (path compression + rank) | ~O(α(n)) | O(n) |
| Merge sort | O(n log n) | O(n) |
| Quick sort (average) | O(n log n) | O(log n) |
| Heap sort | O(n log n) | O(1) |
| Binary search | O(log n) | O(1) |
| BFS / DFS | O(V + E) | O(V) |
| Dijkstra (binary heap) | O((V + E) log V) | O(V) |
| Kahn topological sort | O(V + E) | O(V) |

## Usage

```bash
python -c "from dsa import merge_sort, binary_search; print(merge_sort([3,1,2]), binary_search([1,2,3], 2))"
```

```python
from dsa.graphs import dijkstra

graph = {
    "a": [("b", 1), ("c", 4)],
    "b": [("c", 2)],
    "c": [],
}
print(dijkstra(graph, "a"))  # {'a': 0, 'b': 1, 'c': 3}
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Author

**HeiChan (Chan Hei Lun)** — BEng in Information Engineering, CUHK
[github.com/ChanHei419](https://github.com/ChanHei419)
