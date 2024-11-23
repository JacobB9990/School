#### Question  
2. Given an arbitrary array A, design an algorithm, as efficient as possible, to find the length of the longest increasing subsequence. A valid increasing subsequence may not be contiguous. And, there can be multiple longest increasing subsequences. Time complexity analysis is required.  
- For example, in A = [2, 5, 1, 9, 4, 3, 6], the longest increasing subsequences are [2, 5, 9], [2, 5, 6], [1, 4, 6], and [1, 3, 6]. Thus the length of the longest increasing subsequence in this example is 3.  

#### Answer  
To solve this problem efficiently, we can use binary search to find where each element should go in a list, which improves the algorithm’s performance to a time complexity of `O(n log n)`.

We maintain a list, `sub`, that tracks the smallest possible last value of an increasing subsequence. For each element in the array, we use binary search to determine where it should fit in `sub`. If the element is larger than all values in `sub`, we append it to the end. If not, we replace the element at the found position to keep the subsequences as small as possible.

The time complexity of this approach is `O(n log n)` because:
- We loop through the array once, which takes `O(n)` time.
- For each element, we perform a binary search on `sub`, which takes `O(log n)` time.
- Therefore, the overall time complexity is `O(n log n)`.

Using binary search optimizes the solution and allows it to scale efficiently.


