from stack_singly_linked_list import LinkedList

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

    def push(self, value):
        self.stack.add_to_head(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        value = self.stack.remove_head()
        print(value)
        return value

stack = Stack()

stack.push(100)
stack.push(101)
stack.push(105)
print(stack.pop())
print(stack.pop())
print(stack.pop())

