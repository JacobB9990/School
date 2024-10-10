"""
Linked List Class
"""


class Node:
    def __init__(self, data=None) -> None:
        self.data = data  # Value in node
        self.next = None  # Pointer to next Node


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        # Simple Insert. Needed to create the Link List
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> " if current_node.next else "\n")
            current_node = current_node.next

    def reverse_groups(self, k):
        # Helper function to reverse 'k' nodes in the list
        def reverse(start, k):
            prev, curr = None, start
            while k > 0 and curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        # Check if there are at least k nodes left in the list
        def has_k_nodes(start, k):
            count = 0
            while start and count < k:
                start = start.next
                count += 1
            return count == k

        # Initialize pointers
        dummy = Node(0)
        dummy.next = self.head
        prev_group = dummy
        head = self.head

        while has_k_nodes(head, k):
            group_start = head
            # Move head forward by k nodes
            for i in range(k):
                head = head.next
            # Reverse this group of k nodes
            prev_group.next = reverse(group_start, k)
            group_start.next = head
            # Move the prev_group pointer to the end of the reversed group
            prev_group = group_start

        # Update the head of the linked list
        self.head = dummy.next
