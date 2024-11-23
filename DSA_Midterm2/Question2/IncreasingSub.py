import random

def create_array(n: int) -> list[int]:
    A: set[int] = set()
    
    while len(A) < n:  # Generate random numbers
        rand_int: int = random.randint(1, n * 10)
        A.add(rand_int)

    return list(A)  # Convert to list

def binary_search(sub: list[int], num: int) -> int:
    left: int = 0  # Left pointer
    right: int = len(sub) - 1  # Right pointer
    
    while left <= right:  # While range is valid
        mid: int = (left + right) // 2  # Middle index
        
        if sub[mid] < num: 
            left = mid + 1  # Move left pointer
        else:
            right = mid - 1  # Move right pointer
            
    return left 

def length_of_lis(A: list[int]) -> int:
    sub: list[int] = []  # Result list

    for num in A:  # Loop through A
        pos: int = binary_search(sub, num)  # Find position
        
        if pos == len(sub): 
            sub.append(num) 
        else:
            sub[pos] = num  # Replace value

    return len(sub) 

# Test the function
n: int = int(input('How many elements would you like? '))  # Get number of elements
A: list[int] = create_array(n) 
print("Longest increasing subsequence:", length_of_lis(A)) 