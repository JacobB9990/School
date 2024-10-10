Many functions can be implemented using either iterations or recursion, such as
computing the Fibonacci number. Pleaes argue the pros and cons of both iteration-based and
recursion-based implementations.

### Iteration

- **Pros**
  - **Efficiency**:
    - Iteration generally uses less memory since it doesn’t involve multiple function calls. A Fibonacci iteration can run in linear time (O(n)). If you use a list to store results, the space complexity can be O(n), but if you only keep track of the last two numbers, it can be reduced to O(1).
  - **Predictability**:
    - You know how many elements you’ll be dealing with ahead of time, making it easier to plan for performance.
  - **Better Performance**:
    - As the input size increases, iterative solutions usually perform better than recursive ones.
- **Cons**
  - **Complexity**:
    - For some problems, using iteration can be trickier. The logic might get complicated, especially if you’re nesting loops.

### Recursion

- **Pros**
  - **Simplicity**:
    - The Fibonacci formula is straightforward: F(n) = F(n-1) + F(n-2). It’s easy to understand, especially if you’re familiar with sequences.
  - **Fits Certain Problems**:
    - Recursion works well for problems that fit a divide and conquer approach.
  - **Breaks Down Problems**:
    - It helps in breaking a complex problem into smaller parts, making it easier to solve.
- **Cons**
  - **Inefficiency**:
    - The recursive solution can be slow, with a time complexity of O(2^n).
  - **High Memory Usage**:
    - Each recursive call takes up memory, which can lead to issues like stack overflow for larger inputs.

In summary, while both approaches have their strengths and weaknesses, the choice between iteration and recursion often depends on the specific problem you're tackling.
