# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 2021

@author: Michael Lin
"""


class MaxHeap(dict):
    """
    Build the max heap from scratch
    Modify the format so it is more intuitive
    """
    def __init__(self, max_size):
        super(MaxHeap, self).__init__(self)
        self.__dict__ = self
        self.max_size = max_size
        self.heap = []

    def parent(self, pos):
        """
        Return parent position
        :param pos: position
        :return: parent position
        """
        if pos < 2:
            return pos // 2
        return (pos - 1) // 2

    def left_child(self, pos):
        """
        Return left child position
        :param pos: position
        :return: left child position
        """
        return 2 * pos + 1

    def right_child(self, pos):
        """
        Return right child position
        :param pos: position
        :return: right child position
        """
        return 2 * pos + 2

    def swap(self, pos1, pos2):
        """
        Swap position 1 and position 2
        :param pos1: Position 1
        :param pos2: Position 2
        :return: None
        """
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def is_leaf(self, pos):
        """
        Check whether position will have trouble accessing the heap
        It needs to be in the first half of the list to be able to index left/right child
        :param pos: position
        :return: Boolean True/False
        """
        size = len(self.heap)
        if (size // 2) <= pos <= size-1:
            return True
        return False

    def insert(self, value):
        """
        Insert the value into max heap, then swap
        :param value: insertion value
        :return: None
        """
        if len(self.heap) >= self.max_size:
            return
        self.heap.append(value)
        index = self.heap.index(value)
        while self.heap[index] > self.heap[self.parent(index)]:
            # This step swaps the inserted value, so it doesn't break the max heap format
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def maxHeapify(self, pos):
        """
        Max heapify the tree by swapping with the larger of the two children
        :param pos: position
        :return: None
        """
        if not self.is_leaf(pos):
            if self.heap[pos] < self.heap[(self.left_child(pos))] or \
                    self.heap[pos] < self.heap[(self.right_child(pos))]:
                if self.heap[(self.left_child(pos))] > self.heap[(self.right_child(pos))]:
                    self.swap(pos, self.left_child(pos))
                    self.maxHeapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.maxHeapify(self.right_child(pos))

    def popMax(self):
        """
        Remove the largest value in the max heap
        :return: Largest value in the max heap
        """
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        # Since we swap the last value with the one on top, can just pop the last value in the heap
        self.heap.pop(-1)
        # Re-max heapify the heap
        self.maxHeapify(0)
        return max_val

    def fullHeapify(self):
        """
        Full heapify the heap
        :return: None
        """
        for i in range(0, len(self.heap)//2 - 1):
            self.maxHeapify(i)

    def print(self):
        """
        Print the heap in a list format
        :return: Heap in list format
        """
        print(self.heap)

    def print_format(self):
        """
        Print the heap in a tree format
        :return: Heap in tree format
        """
        for i in range(0, len(self.heap) // 2):
            try:
                right = str(self.heap[2 * i + 2])
            except IndexError:
                right = "NULL"
            print(" PARENT: " + str(self.heap[i]) + " LEFT CHILD: " + str(self.heap[2 * i + 1]) + " RIGHT CHILD: " +
                  right)


def main():
    max_heap = MaxHeap(10)
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
    max_heap.print()
    print("\nBEFORE MAX REMOVAL: ")
    max_heap.print_format()
    print("\nMAX VALUE POP: {}".format(max_heap.popMax()))
    print("\nAFTER MAX REMOVAL: ")
    max_heap.print_format()
    print("\nMAX VALUE POP: {}".format(max_heap.popMax()))
    print("\nAFTER MAX REMOVAL: ")
    max_heap.print_format()


if __name__ == '__main__':
    main()
