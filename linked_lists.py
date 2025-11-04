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
    def search(self, data):
        current = self.head
        while current:  # traverse and compare with the target data
            if current.data == data:
                return True
            current = current.next
        return False
    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:  # Node to delete is not the head
                    prev.next = current.next
                else:  # Node to delete is the head
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def is_empty(self):
        return self.head is None



sll = SinglyLinkedList()
sll.insert(10)
sll.insert(20)
sll.insert(30)
print("Traversing the list:")
sll.traverse()
print("\nSearching for 20:", sll.search(20))
print("Searching for 40:", sll.search(40))
sll.delete(20)
print("\nTraversing the list after deleting 20:")
sll.traverse()
