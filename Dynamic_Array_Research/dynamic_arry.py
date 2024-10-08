import ctypes  # How we can create an array


class DynamicArray(object):  # objects mean any value type (int, str, ...)
    def __init__(self, initial_capacity=16):
        self.n = 0  # Number of elements (init with 0)
        self.capacity = initial_capacity  # Gives cap 16 as default
        self.A = self.make_array(self.capacity)  # Will explain soon

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of range")
        return self.A[index]

    def __str__(self):
        return "[" + ", ".join(str(self.A[i]) for i in range(self.n)) + "]"

    def findCapacity(self):
        return self.capacity

    def append(self, ele):  # Element is the value you are adding
        if self.n == self.capacity:  # Makes sure there is room
            self._resize(int(self.capacity * 2))  # Capacity times 2
        self.A[self.n] = ele  # That index now is equal to ele
        self.n += 1  # Adds on total elements

    def insertAt(self, index, value):
        if index < 0 or index > self.n:
            raise IndexError("Index out of range")
        if self.n == self.capacity:
            self._resize(int(self.capacity * 1.5))
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
        self.n -= 1
        if self.n < self.capacity // 4:
            self._resize(max(16, int(self.capacity * 0.5)))

    def delete(self):
        if self.n == 0:
            raise IndexError("Array is empty")
        self.n -= 1
        if self.n < self.capacity // 4:
            self._resize(max(16, int(self.capacity * 0.5)))

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):  # self.A becomes the return value
        return (new_cap * ctypes.py_object)()  # returns array

    def extend(self, *args):
        if self.n + len(args) > self.capacity:
            new_cap = max(self.capacity * 2, self.n + len(args))
            self._resize(new_cap)
        for i in args:
            self.append(i)
