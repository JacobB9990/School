import time


# Recursion-based
def recursion_fib(n: int) -> int:
    if n == 1:
        return 0  # Base case: fib(1) is 0
    elif n == 2:
        return 1  # Base case: fib(2) is 1
    else:
        return recursion_fib(n - 1) + recursion_fib(n - 2)


# Iteration-based
def iteration_fib(n: int) -> int:
    starting: list[int] = [
        0,
        1,
    ]

    for i in range(1, n + 1):
        result: int = starting[i] + starting[i - 1]
        starting.append(result)
    return result


# Runs the function and returns final time and the result
def get_time(func, n: int) -> tuple[float, int]:
    start: float = time.perf_counter()
    result: int = func(n)
    end: float = time.perf_counter()
    final_time: float = end - start
    return final_time, result


# Simple error checking
while True:
    try:
        calculate_term = int(input("Please input the nth term you want: "))
        break
    except ValueError:
        raise ValueError("Please enter a valid integer")

if calculate_term == 1 or calculate_term == 0:
    print("Fib(0) = 0 and Fib(1) = 1")
    exit()

iteration = get_time(iteration_fib, calculate_term - 1)
recursion = get_time(recursion_fib, calculate_term + 1)

print(f"Iteration Based (result, time(s)): {iteration}")
print(f"Recursion Based (result, time(s)): {recursion}")
