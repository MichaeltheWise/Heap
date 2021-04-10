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
