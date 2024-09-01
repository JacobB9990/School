"""
Dynamic Array
"""
import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0  # actual number of elements
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError

        return self.A[index]

    def append(self, value):
        pass

    def insertAt(self, index, value):
        pass

    def remove(self, value):
        pass

    def delete(self):
        pass

    def _resize(self):
        pass

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


a = DynamicArray()
