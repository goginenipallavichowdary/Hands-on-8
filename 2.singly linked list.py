class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage and output
linked_list = SinglyLinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)

print("Linked List:")
linked_list.print_list()
print("Size:", linked_list.get_size())
print("Is 20 in the list?", linked_list.search(20))
linked_list.delete(20)
print("After deleting 20:")
linked_list.print_list()
print("New size:", linked_list.get_size())

#output:
#Linked List:
#5 -> 10 -> 20 -> None
#Size: 3
#Is 20 in the list? True
#After deleting 20:
#5 -> 10 -> None
#New size: 2
