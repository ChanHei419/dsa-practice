import unittest

from dsa.graphs import bfs, dfs, dijkstra, has_cycle, topological_sort

SAMPLE = {
    "a": [("b", 1), ("c", 4)],
    "b": [("c", 2)],
    "c": [],
}

DAG = {
    "shirt": [("tie", 1), ("belt", 1)],
    "tie": [("jacket", 1)],
    "belt": [("jacket", 1)],
    "jacket": [],
    "socks": [("shoes", 1)],
    "shoes": [],
}

CYCLIC = {
    "a": [("b", 1)],
    "b": [("c", 1)],
    "c": [("a", 1)],
}


class TraversalTests(unittest.TestCase):
    def test_bfs_order(self):
        self.assertEqual(bfs(SAMPLE, "a"), ["a", "b", "c"])

    def test_dfs_order(self):
        self.assertEqual(dfs(SAMPLE, "a"), ["a", "b", "c"])

    def test_dfs_respects_neighbour_order(self):
        graph = {"a": [("b", 1), ("c", 1)], "b": [], "c": []}
        self.assertEqual(dfs(graph, "a"), ["a", "b", "c"])


class DijkstraTests(unittest.TestCase):
    def test_shortest_distances(self):
        self.assertEqual(dijkstra(SAMPLE, "a"), {"a": 0, "b": 1, "c": 3})

    def test_unreachable_nodes_are_absent(self):
        graph = {"a": [("b", 1)], "b": [], "island": []}
        self.assertNotIn("island", dijkstra(graph, "a"))


class TopologicalSortTests(unittest.TestCase):
    def test_kahn_orders_dependencies_before_dependents(self):
        order = topological_sort(DAG)
        self.assertEqual(len(order), 6)
        self.assertLess(order.index("tie"), order.index("jacket"))
        self.assertLess(order.index("belt"), order.index("jacket"))

    def test_cycle_raises(self):
        with self.assertRaises(ValueError):
            topological_sort(CYCLIC)

    def test_has_cycle(self):
        self.assertTrue(has_cycle(CYCLIC))
        self.assertFalse(has_cycle(DAG))


if __name__ == "__main__":
    unittest.main()
