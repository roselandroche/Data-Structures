from queue_singly_linked_list import LinkedList

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
class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.add_to_tail(value)

    def dequeue(self):
        value = self.queue.remove_head()
        return value
