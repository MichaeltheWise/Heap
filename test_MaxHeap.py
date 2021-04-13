import MaxHeap
import unittest
import heapq
import numpy as np


class TestMaxHeap(unittest.TestCase):
    def test_popMax(self):
        max_heap = MaxHeap.MaxHeap(10)
        max_heap.insert(5)
        max_heap.insert(14)
        max_heap.insert(23)
        max_heap.insert(32)
        max_heap.insert(41)
        max_heap.insert(87)
        max_heap.insert(90)
        max_heap.insert(50)
        max_heap.insert(64)
        max_heap.insert(53)
        max_heap.fullHeapify()

        self.assertEqual(max_heap.popMax(), 90)
        self.assertEqual(max_heap.popMax(), 87)

    @unittest.skip
    def test_popMax_benchmark(self):
        max_heap = MaxHeap.MaxHeap(10)
        max_heap.insert(5)
        max_heap.insert(14)
        max_heap.insert(23)
        max_heap.insert(32)
        max_heap.insert(41)
        max_heap.insert(87)
        max_heap.insert(90)
        max_heap.insert(50)
        max_heap.insert(64)
        max_heap.insert(53)
        max_heap.fullHeapify()

        input_list = np.array([5, 14, 23, 32, 41, 87, 90, 50, 64, 53])
        input_list *= -1
        expected = list(input_list)
        heapq.heapify(expected)
        expected = [-1 * _ for _ in expected]
        # Using minHeap heapify to reverse create the max heap tree yields a different result
        # expected = [90 64 87 50 53 5 23 14 32 41]
        # actual = [90 64 87 50 53 14 41 5 32 23]
        self.assertEqual(expected, max_heap)
