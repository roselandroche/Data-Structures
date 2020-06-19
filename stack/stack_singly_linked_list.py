class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
    
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 1 if head is not None else 0
    
    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        if not self.head:
            return None
        self.length -= 1
        if self.head.get_next() is None:
            # get a reference to the head
            head_value = self.head.value
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.get_next()
        return head_value

    # def remove_tail(self):
    #     if not self.tail:
    #         return None
    #     self.length -= 1
    #     for item in range(self.length + 1):
    #         if item.next_node == self.tail:
    #             new_tail = item
    #             new_tail.next_node = None
    #             self.tail = new_tail