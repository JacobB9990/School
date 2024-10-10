from LinkedList import *

linked_list = LinkedList()
len_list = 10

for i in range(len_list, 0, -1):
    linked_list.insert(i)

linked_list.printLL()

linked_list.reverse_groups(5)
linked_list.printLL()
