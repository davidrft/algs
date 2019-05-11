class MinHeap:
    def __init__(self, L=[]):
        self.heap = []

        for element in L:
            self.insert(element)

    def __len__(self):
        return len(self.heap)

    def insert(self, val) -> None:
        if val is None:
            raise TypeError('Inserted value cannot be None')

        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, i: int) -> None:
        child, parent = i, i // 2

        while self.heap[child] < self.heap[parent]:
            self.heap[child], self.heap[parent] = self.heap[parent],
            self.heap[child]
            child, parent = parent, parent // 2

    def bubble_down(self, i: int) -> None:
        child, parent = self.min_child(i), i

        while child != -1 and self.heap[parent] > self.heap[child]:
            self.heap[child], self.heap[parent] = self.heap[parent],
            self.heap[child]
            child, parent = self.min_child(child), parent

    def min_child(self, i: int) -> int:
        l, r = i * 2, (i * 2) + 1

        if l >= len(self.heap):
            return -1

        if r >= len(self.heap):
            return l

        return l if self.heap[l] < self.heap[r] else r

    def pop_min(self):
        val = self.heap[0]

        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
        else:
            self.heap.pop()

        self.bubble_down(0)
        return val

    def peek_min(self):
        return heap[0]
