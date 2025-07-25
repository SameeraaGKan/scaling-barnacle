# A Node class might commonly look like the following.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # Constructor.
    def __init__(self):
        # The first node in the linked list.
        # The head is either a Node object or None if the list is empty.
        self.head = None

    # Method. Adds a new node with the specific data value to the beginning of the linked list.
    def add_first(self, value):
        pass

    # Method. Adds a node with specified value to the end of the list.
    def append(self, value):
        pass

    # Method. Returns the length of the list.
    def length(self):
        pass

    # Method. Returns the value at a given index in the linked list.
    # Index count starts at 0.
    # Returns None if there are fewer nodes in the linked list than the index value.
    def get_at_index(self, index):
        pass


# Linked List Traversal

def traverse(head):
        current = head
        while current:
            # Perform operations on the current node (e.g., print the value)
            current = current.next # Move to the next node