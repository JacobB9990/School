#### Question
1. Given an arbitrary array A of integers, please design an algorithm, as efficient as possible, that constructs another array B of the same size (i.e., |B|=|A|), where B[i] is the number of elements in A on the right side of A[i] and smaller than A[i]. Time complexity analysis is required.
- For example, A = [3,1,4,2], B = [2,0,1,0].

#### Answer  
There are different ways to solve this problem, but the most efficient approach uses a modified merge sort to reduce the time complexity to `O(n log n)`. The idea is to sort the array while tracking how many elements on the right side of each element are smaller than it.

In the merge sort approach:
- The array is divided into two halves recursively, creating a recursion tree of depth `O(log n)`.
- During the merge phase, the two halves are merged in `O(n)` time at each recursion level.
- Since we perform `O(n)` work at each of the `O(log n)` levels, the total time complexity is `O(n log n)`.

The counting of smaller elements happens during the merge step, so it doesn’t add any extra complexity beyond the standard merging process, keeping the overall time complexity at `O(n log n)`.

This approach is faster than the `O(n^2)` solution and more efficient overall.