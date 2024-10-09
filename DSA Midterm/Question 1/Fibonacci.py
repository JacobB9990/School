def main() -> None:
    # Recursion-based
    def rec_fib(n: int) -> int:
        if n == 1:
            return 0  # Base case: fib(1) is 0
        elif n == 2:
            return 1  # Base case: fib(2) is 1
        else:
            return rec_fib(n - 1) + rec_fib(n - 2)

    def print_rec_fibonacci(k: int, current: int = 1) -> int:
        if current > k:
            return 0
        print(rec_fib(current))
        return print_rec_fibonacci(k, current + 1)

    # Iteration-based
    def iter_fib(k: int) -> int:
        starting: list[int] = [
            0,
            1,
        ]  # Using a list is helpful, but can be a little slower.

        for i in range(1, k + 1):
            result: int = starting[i] + starting[i - 1]
            starting.append(result)
            print(starting[i])

        return result

    # Testing
    calculate_term: int = 10

    print_rec_fibonacci(calculate_term)
    iter_fib(calculate_term - 1)


if __name__ == "__main__":
    main()
