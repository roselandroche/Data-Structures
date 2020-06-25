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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        # add the first node to the queue
        # while queue is not empty, 
            # remove the first node from the queue (pop and save to variable)
            # print the removed node (via variable)
            # add all children into queue
            # repeat
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty:
            # get the current node from the top of the stack
            # print that node
            # add right child then left child to stack - ORDER MATTERS
            # repeat - remove left child, print left child, add right child and left child to stack
            # 
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

