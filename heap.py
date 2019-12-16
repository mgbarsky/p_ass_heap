import numpy as np

class HeapError(Exception):
    def __init__(self, title, message):
        self.title = title
        self.msg = message

    def __repr__(self):
        return "{0}: {1}".format(self.title, self.msg)

class MinHeap:
    def __init__(self, capacity):
        self.a = np.zeros(capacity)
        self.capacity = capacity
        self.length = 0

    def insert(self, value):
        if self.length == self.capacity:
            raise HeapError ("Insertion failed", "heap is full")

        self.length += 1
        self.a[self.length - 1] = value
        self.sift_up(self.length - 1)

    def get_min(self):
        if self.length == 0:
            raise HeapError ("Min failed", "heap is empty")

        return self.a[0]

    def sift_up(self, index):
        if index == 0:
            return

        parent = (index - 1) // 2

        if self.a[parent] > self.a[index]:
            tmp = self.a[parent]
            self.a[parent] = self.a[index]
            self.a[index] = tmp

            self.sift_up(parent)


    def extract_min(self):
        if self.length == 0:
            HeapError ("Min failed", "heap is empty")

        result = self.a[0]
        self.a[0] = self.a[self.length - 1]
        self.length -= 1

        if self.length == 0:
            return

        self.sift_down(0)
        return result

    def sift_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2

        if left >= self.length and right >= self.length:
            return

        min_index = left
        if right < self.length and self.a[left] > self.a[right]:
            min_index = right

        if self.a[index] > self.a[min_index]:
            tmp = self.a[min_index]
            self.a[min_index] = self.a[index]
            self.a[index] = tmp

            self.sift_down(min_index)

    def print_heap(self, index, indent=0):
        if index >= self.length:
            return

        print(" "*indent, self.a[index])
        left = 2 * index + 1
        self.print_heap(left, indent +1)
        right = 2 * index + 2
        self.print_heap(right, indent + 1)

if __name__ == "__main__":
    heap = MinHeap(6)

    heap.insert(4)
    heap.insert(7)
    heap.insert(3)
    heap.insert(11)
    heap.insert(2)
    heap.insert(6)

    heap.print_heap(0)

    print("----------------------")
    a = heap.extract_min()

    heap.print_heap(0)



