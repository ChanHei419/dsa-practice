import unittest

from dsa.searching import (
    binary_search,
    count_occurrences,
    lower_bound,
    upper_bound,
)


class BinarySearchTests(unittest.TestCase):
    def test_finds_present_values(self):
        data = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 9), 4)

    def test_missing_value_returns_minus_one(self):
        self.assertEqual(binary_search([1, 3, 5], 4), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)


class BoundTests(unittest.TestCase):
    data = [1, 2, 2, 2, 5]

    def test_lower_bound(self):
        self.assertEqual(lower_bound(self.data, 2), 1)
        self.assertEqual(lower_bound(self.data, 0), 0)
        self.assertEqual(lower_bound(self.data, 6), 5)

    def test_upper_bound(self):
        self.assertEqual(upper_bound(self.data, 2), 4)
        self.assertEqual(upper_bound(self.data, 5), 5)

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences(self.data, 2), 3)
        self.assertEqual(count_occurrences(self.data, 5), 1)
        self.assertEqual(count_occurrences(self.data, 99), 0)


if __name__ == "__main__":
    unittest.main()
