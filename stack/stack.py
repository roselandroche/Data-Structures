import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# AS AN ARRAY STRUCTURE - LIFO

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop(0)
#         else:
#             return None

# AS A LINKED LIST - LIFO


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def __len__(self):
        return len(self.stack)
        # if self.head is None and self.tail is None:
        #     return 0

        # if self.head.next_node is self.tail:
        #     return 2

        # current_node = self.head
        # length = 1

        # while current_node is not self.tail:
        #     length += 1
        #     current_node = current_node.next_node
        # return length

    def push(self, value):
        self.stack.add_to_head(value)

    def pop(self):
        self.stack.remove_head()
        # if not self.head:
        #     return None
        # if self.head.next_node is None:
        #     head_value = self.head.value
        #     self.head = None
        #     self.tail = None
        #     return head_value
        # head_value = self.head.value
        # self.head = self.head.next_node
        # return head_value
        