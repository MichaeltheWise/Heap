# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 2021

@author: Michael Lin
"""


class MinHeap(dict):
    def __init__(self, max_size):
        super(MinHeap, self).__init__(self)
        self.__dict__ = self
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * (max_size + 1)

    def parent(self, pos):
        # Parent is index / 2 for both min heap and max heap
        return pos // 2

    def left_child(self, pos):
        # Left child is 2 * index + 1
        return pos * 2

    def right_child(self, pos):
        # Right child is 2 * index + 2
        return pos * 2 + 1

    def is_leaf(self, pos):
        if (self.size // 2) < pos <= self.size:
            return True
        return False

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def minHeapify(self, pos):
        if not self.is_leaf(pos):
            if self.heap[pos] > self.heap[self.left_child(pos)] or self.heap[pos] > self.heap[self.right_child(pos)]:
                # Swap with the lower of the two: left child and right child
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.minHeapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.minHeapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element

        curr = self.size

        while self.heap[curr] < self.heap[self.parent(curr)]:
            # Compare the new element with its parent, if it is smaller then swap with parent
            # Keep doing this operation until we reach the root
            # This operation basically moves the node up the tree
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    def remove(self):
        # Remove and return the value selected
        popped = self.heap[1]
        # Move the maximum number to the root
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        # Swap with its the smaller-valued children
        self.minHeapify(1)
        return popped

    def print(self):
        print(self.heap)

    def print_format(self):
        for i in range(1, (self.size // 2) + 1):
            try:
                right = str(self.heap[2 * i + 1])
            except IndexError:
                right = "NULL"
            print(" PARENT: " + str(self.heap[i]) + " LEFT CHILD: " + str(self.heap[2 * i]) + " RIGHT CHILD: " +
                  right)


def main():
    min_heap = MinHeap(10)
    min_heap.insert(5)
    min_heap.insert(14)
    min_heap.insert(23)
    min_heap.insert(32)
    min_heap.insert(41)
    min_heap.insert(87)
    min_heap.insert(90)
    min_heap.insert(50)
    min_heap.insert(64)
    min_heap.insert(53)
    print("\nBEFORE MIN REMOVAL: ")
    min_heap.print_format()
    min_heap.remove()
    print("\nAFTER MIN REMOVAL: ")
    min_heap.print_format()
    min_heap.remove()
    print("\nAFTER MIN REMOVAL: ")
    min_heap.print_format()


if __name__ == '__main__':
    main()
