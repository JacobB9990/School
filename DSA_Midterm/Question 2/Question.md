Given a singly linked list of numbers. Starting from the head, consider each consecutive elements as a group. The leftovers (must be less than ) are considered as a group. Please design an algorithm to reverse all elements in each group. Your algorithm should be as efficient as possible in both time and space. And, please analyze the time complexity and space complexity.

- **Example**: Given 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 and k = 3. In this example, 1 → 2 → 3 is a group, 4 → 5 → 6 is another group, 7 → 8 and is the leftover group. The output of your algorithm should be. 3 → 2 → 1 → 5 → 5 → 4 → 8 → 7.

### Time Complexity

1. **Insertion**:

   - Each insertion is O(1) because it involves creating a new node and adjusting the pointers.
   - If you insert n nodes, the total time complexity for the insertions is O(n).

2. **Printing**:

   - Printing the linked list traverses all nodes once, which takes O(n).

3. **Reversing Groups**:

   - The method uses two main operations:
     - **Checking for k nodes**: The has_k_nodes function traverses the list to check if there are at least k nodes left. In the worst case, this traverses the entire list, resulting in O(n) time complexity.
     - **Reversing k nodes**: The reverse function also traverses k nodes to reverse them, which takes O(k). However, since this is called multiple times, we need to consider how many times it will be called.
   - The while loop in reverse_groups continues until there are no more complete groups of k nodes. For a list of n nodes, this will involve approximately n/k iterations.
   - In each iteration, we do a check (O(n)) and reverse (O(k)).
   - Thus, the total complexity for reversing the entire list is:
     - **O(n)** (for the while loop running n/k times) × O(k) (for reversing each group) = (O(n)).

Putting it all together, the total time complexity for the reverse_groups method is (O(n)).

### Overall Time Complexity

- Overall, the time complexity for creating, printing, and reversing the linked list is:
  - (O(n)) + O(n) + O(n) = O(n)

### Space Complexity

1. **Insertion and Print**:

   - Both the insert and printLL methods use a constant amount of space (O(1)) for pointers and temporary variables.

2. **Reverse Groups**:

   - The reverse_groups method also primarily uses constant space for pointers (prev, curr, next_node, etc.).
   - The space used does not scale with the input size since no additional data structures are created that grow with n.

The only additional space used is for the dummy node, which is also constant.
