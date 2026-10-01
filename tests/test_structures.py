import unittest

from dsa.structures import LinkedList, MinHeap, Queue, Stack, UnionFind


class StackTests(unittest.TestCase):
    def test_lifo_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(len(stack), 1)

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            Stack().pop()


class QueueTests(unittest.TestCase):
    def test_fifo_order(self):
        queue = Queue()
        queue.enqueue("a")
        queue.enqueue("b")
        self.assertEqual(queue.dequeue(), "a")
        self.assertEqual(queue.dequeue(), "b")
        self.assertTrue(queue.is_empty())

    def test_dequeue_empty_raises(self):
        with self.assertRaises(IndexError):
            Queue().dequeue()


class LinkedListTests(unittest.TestCase):
    def test_append_prepend_and_iterate(self):
        values = LinkedList()
        values.append(2)
        values.append(3)
        values.prepend(1)
        self.assertEqual(values.to_list(), [1, 2, 3])
        self.assertEqual(len(values), 3)

    def test_remove_head_middle_and_missing(self):
        values = LinkedList()
        for number in (1, 2, 3):
            values.append(number)
        self.assertTrue(values.remove(1))
        self.assertTrue(values.remove(3))
        self.assertFalse(values.remove(99))
        self.assertEqual(values.to_list(), [2])


class MinHeapTests(unittest.TestCase):
    def test_pops_in_sorted_order(self):
        heap = MinHeap()
        for value in (5, 1, 3, 2, 4):
            heap.push(value)
        self.assertEqual(heap.peek(), 1)
        self.assertEqual([heap.pop() for _ in range(5)], [1, 2, 3, 4, 5])

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            MinHeap().pop()


class UnionFindTests(unittest.TestCase):
    def test_union_and_components(self):
        union_find = UnionFind(5)
        self.assertTrue(union_find.union(0, 1))
        self.assertTrue(union_find.union(3, 4))
        self.assertFalse(union_find.union(0, 1))
        self.assertTrue(union_find.connected(0, 1))
        self.assertFalse(union_find.connected(0, 3))
        self.assertEqual(union_find.components, 3)


if __name__ == "__main__":
    unittest.main()
