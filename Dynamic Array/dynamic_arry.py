import ctypes

class DynamicArray(object):
    def __init__(self, initial_capacity=16):  # Larger initial capacity
        self.n = 0
        self.capacity = initial_capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of range")
        return self.A[index]

    def __str__(self):
        return "[" + ", ".join(str(self.A[i]) for i in range(self.n)) + "]"

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = ele
        self.n += 1

    def insertAt(self, index, value):
        if index < 0 or index > self.n:
            raise IndexError("Index out of range")
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]
        self.A[index] = value
        self.n += 1

    def remove(self, index):
        if self.n == 0:
            raise IndexError("Array is empty")
        if index < 0 or index >= self.n:
            raise IndexError("Index out of range")
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]
        self.A[self.n - 1] = None
        self.n -= 1

    def delete(self):
        if self.n == 0:
            raise IndexError("Array is empty")
        self.A[self.n - 1] = None
        self.n -= 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def extend(self, *args):
        if self.n + len(args) > self.capacity:
            new_cap = max(self.capacity * 2, len(args))
            self._resize(new_cap)
        for i in args:
            self.append(i)
