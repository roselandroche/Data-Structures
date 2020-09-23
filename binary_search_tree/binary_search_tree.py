from bst_queue import Queue
from bst_stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value and self.left is None:
            self.left = BSTNode(value)
        elif self.value > value and self.left is not None:
            self.left.insert(value)
        elif self.value <= value and self.right is None:
            self.right = BSTNode(value)
        elif self.value <= value and self.right is not None:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value is not None:
            if self.left:
                self.left.for_each(fn)
            fn(self.value)
            if self.right:
                self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # JUST REWRITE FOR EACH
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        bft_queue = Queue()
        # add the first node to the queue
        bft_queue.enqueue(node)
        # while queue is not empty, 
            # remove the first node from the queue (pop and save to variable)
            # print the removed node (via variable)
            # add all children into queue
            # repeat
        while len(bft_queue) > 0:
            current = bft_queue.dequeue()
            print(current.value)
            if current.left:
                bft_queue.enqueue(current.left)
            if current.right:
                bft_queue.enqueue(current.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        dft_stack = []
        # add the first node to the stack
        dft_stack.append(node)
        # while the stack is not empty:
            # get the current node from the top of the stack
            # print that node
            # add right child then left child to stack - ORDER MATTERS
            # repeat - remove left child, print left child, add right child and left child to stack
        while len(dft_stack) > 0:
            current = dft_stack.pop()
            print(current.value)
            if current.right:
                dft_stack.append(current.right)
            if current.left:
                dft_stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# example = BSTNode(40)
# example.insert(36)
# example.insert(77)
# example.insert(2)
# example.insert(29)
# example.bft_print(example)

# stack_ex = BSTNode(53)
# stack_ex.insert(98)
# stack_ex.insert(34)
# stack_ex.insert(56)
# stack_ex.insert(12)
# stack_ex.dft_print(stack_ex)