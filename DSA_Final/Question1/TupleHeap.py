def sort_by_value(pairs):
    def get_value(pair):
        return pair[1]

    pairs.sort(key=get_value)


def build_heap(pairs):
    sort_by_value(pairs)

    def heapify(arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left][0] < arr[smallest][0]:
            smallest = left
        if right < n and arr[right][0] < arr[smallest][0]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify(arr, n, smallest)

    n = len(pairs)
    for i in range(n // 2 - 1, -1, -1):
        heapify(pairs, n, i)

    return pairs


A = [(5, 6), (1, 2), (3, 4), (9, 1), (6, 9), (2, 8), (4, 3), (8, 5)]
heap = build_heap(A)
print("Heap (array):", heap)
