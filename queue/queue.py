"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# AS AN ARRAY - FIFO

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         # ADD TO END OF QUEUE
#         return self.storage.append(value)

#     def dequeue(self):
#         # REMOVE AND RETURN FROM END OF QUEUE
#         if len(self.storage) > 0:
#             return self.storage.pop(0)
#         else:
#             return None

# AS A LINKED LIST - FIFO
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __len__(self):
        if self.head is None and self.tail is None:
            return 0
        current_node = self.head
        length = 1
        while current_node is not self.tail:
            length += 1
            current_node = current_node.next_node
        return length

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
