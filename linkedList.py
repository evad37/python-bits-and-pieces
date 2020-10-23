class Node:
    """A node for a linked list, each consisting of a value and a pointer to the next node"""
    def __init__(self, val):
        """Constructor for a node with a value"""
        self.val = val
        self.next = None 

    def __str__(self):
        """Returns the node's value as a string"""
        return str(self.val)

'''
# Example use of nodes:
node1 = Node(5)
node2 = Node(7)
node1.next = node2
node3 = Node(99)
node2.next = node3
print(node1.next.next) # prints "99"
'''

class LinkedList:
    """A linked list of nodes"""
    
    def __init__(self, firstVal_or_node):
        """Constructor for starting a linked list with a value or a node"""
        if isinstance(firstVal_or_node, Node):
            self.firstNode = firstVal_or_node
        self.firstNode = Node(firstVal_or_node)

    def add(self, val):
        """Add a value to the end of the list"""
        node = self.firstNode
        # Find the last node in the list
        while node.next is not None:
            node = node.next
        # Append a new node
        node.next = Node(val)

    def __str__(self):
        """Returns the string representation of the linked list"""
        # Start with the first value
        output = str(self.firstNode)
        # For each subsequent node, add an arrow and the value
        node = self.firstNode.next
        while node is not None:
            output = output + f" --> {node}"
            node = node.next
        return output

    def removeDuplicates(self):
        """Removes any duplicate values from the linked list"""
        # Check each node to see if any subsequent nodes are duplicates
        node = self.firstNode
        while node is not None:
            # Look through the rest of the linked list
            currentNode = node
            while currentNode.next is not None:
                if currentNode.next.val == node.val:
                    # Next value is a duplicate, skip it
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next
            node = node.next

'''
# Example use of a linked list
ll = LinkedList(5)
ll.add(7)
ll.add(5)
ll.add(7)
ll.add(5)
ll.add(2)
ll.add(22)

print(f"Original list:      {ll}")
# prints "Original list:      5 --> 7 --> 5 --> 7 --> 5 --> 2 --> 22"

ll.removeDuplicates()
print(f"Without duplicates: {ll}")
# prints "Without duplicates: 5 --> 7 --> 2 --> 22"
'''
