import random

class Node:
    """A node for a binary tree"""
    def __init__(self, val):
        """Constructor for a node with a value"""
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        """Returns the node's value as a string"""
        return str(self.val)

    def printTree(self, prefix="", symbol="-"):
        """Prints a text-based graphical respresentation of the binary tree"""
        if len(prefix) == 0:
            print(self, "(ROOT)")
        else:
            print(f"{prefix}--{symbol}--> {self}")
        if self.right is not None:
            self.right.printTree(prefix+"      "+("|"if self.left is not None else " "), "R")
        if self.left is not None:
            self.left.printTree(prefix+"       ", "L")
             
    def insert(self, val):
        if val < self.val:
            # insert on left
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            #insert of right
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        
root = Node(25)
for i in range(20):
    root.insert(random.randrange(50))
root.printTree()

