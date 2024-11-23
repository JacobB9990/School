import random


def create_array(n: int) -> list[int]:
    A: set[int] = set()
    
    while len(A) < n:
        rand_int = random.randint(1, n*10)
        A.add(rand_int)

    return list(A)


def find_small_ele(n: int, A: list[int]) -> list[int]:
    B: list[int] = []
    curr_index: int = 0
    
    while len(B) < n:
        count = 0
        for i in range(curr_index + 1, n):
            if A[curr_index] > A[i]:
                count += 1
        
        B.append(count)
        curr_index += 1  

    return B


n = 40
# Testing
A = create_array(n)
B = find_small_ele(n, A)
print(A)
print(B)
