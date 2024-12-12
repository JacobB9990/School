def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Comparisons
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapify_up(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break


def delete_any(arr, n, value):
    try:
        index = arr.index(value)
    except ValueError:
        raise ValueError(f"Element not found in the heap.")

    arr[index] = arr[n - 1]
    arr.pop()
    n -= 1

    heapify(arr, n, index)
    if arr[index] < arr[(index - 1) // 2] if index > 0 else True:
        heapify_up(arr, index)

    return n


array = [5, 1, 3, 9, 6, 2, 4, 8]
build_heap(array)
print("Heap before deletion:", array)

n = len(array)
n = delete_any(array, n, 6)

print("Heap after deletion:", array)
