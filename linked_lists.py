class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head: # Special case: if list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next: # traverse to the last node
                current = current.next
            current.next = new_node