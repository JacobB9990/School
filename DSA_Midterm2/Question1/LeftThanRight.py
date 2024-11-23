import random


def create_array(n: int) -> list[int]:
    A: set[int] = set()
    
    while len(A) < n: # Generate random numbers
        rand_int: int = random.randint(1, n * 10)
        A.add(rand_int)

    return list(A)  # Convert to list


def merge_sort_with_counts(arr: list[int], indices: list[int], result: list[int]) -> list[int]:
    # Base case
    if len(indices) <= 1:
        return indices

    mid: int = len(indices) // 2  # Middle point
    # Recursion
    left: list[int] = merge_sort_with_counts(arr, indices[:mid], result)
    right: list[int] = merge_sort_with_counts(arr, indices[mid:], result)

    merged: list[int] = []  # Merged list
    i: int = 0  # Left pointer
    j: int = 0  # Right pointer
    count_right_smaller: int = 0  # Count of smaller elements

    # Merging loop
    while i < len(left) or j < len(right):
        if j >= len(right) or (i < len(left) and arr[left[i]] <= arr[right[j]]):
            result[left[i]] += count_right_smaller  # Update count
            merged.append(left[i])  # Add left index
            i += 1  # Move left pointer
        else:
            count_right_smaller += 1  # Increment count
            merged.append(right[j])  # Add right index
            j += 1  # Move right pointer

    return merged 


n: int = int(input('How many elements would you like? ')) # Get number of elements
A: list[int] = create_array(n) # Create random array
result: list[int] = [0] * n # Result list
indices: list[int] = list(range(n)) # Index list
merge_sort_with_counts(A, indices, result)

# Output
print("A = ", A)
print("B = ", result)