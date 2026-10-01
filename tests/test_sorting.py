import random
import unittest

from dsa.sorting import heap_sort, insertion_sort, merge_sort, quick_sort


class SortingTests(unittest.TestCase):
    algorithms = [insertion_sort, merge_sort, quick_sort, heap_sort]

    def test_sorts_typical_input(self):
        data = [5, 3, 8, 1, 9, 2, 7]
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(data), [1, 2, 3, 5, 7, 8, 9])

    def test_handles_duplicates(self):
        data = [4, 2, 4, 1, 2, 4]
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(data), [1, 2, 2, 4, 4, 4])

    def test_empty_and_single(self):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([]), [])
                self.assertEqual(algorithm([1]), [1])

    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                algorithm(data)
                self.assertEqual(data, [3, 1, 2])

    def test_matches_sorted_on_random_data(self):
        random.seed(42)
        data = [random.randint(0, 100) for _ in range(50)]
        expected = sorted(data)
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(data), expected)


if __name__ == "__main__":
    unittest.main()
