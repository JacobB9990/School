#### Question
2. (50 pts) For an array-based binary min-heap, please implement the operation DELETE which removes an element from the heap, and analyze the running time.

#### Answer
- The `DELETE` function for an array-based binary min-heap wasn’t too hard to implement. First, we find the index of the element to delete, which takes O(n) time since we need to search through the entire array. After finding the element, we swap it with the last element and remove the last element, both of which take O(1) time. Finally, we restore the heap property by calling `heapify`, which takes O(log n) time in the worst case. So, the overall time complexity of the `DELETE` function is O(n) because of the search, but the heapify step only adds O(log n). Overall, it was a pretty straightforward addition to the heap implementation.
