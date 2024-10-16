class ListNode:  
    def __init__(self, value):  
        self.value = value  
        self.next_node = None  

class LinkedList:  
    def __init__(self):  
        self.head_node = None  

    def insert_at_start(self, value):  
        new_node = ListNode(value)  
        new_node.next_node = self.head_node  
        self.head_node = new_node  
    def display(self): 
        current_node = self.head_node  
        while current_node:  
            print(current_node.value)  
            current_node = current_node.next_node  

# Example 
linked_list_instance = LinkedList()
linked_list_instance.insert_at_start(1)  
linked_list_instance.insert_at_start(2)  
linked_list_instance.display()

"""2
1"""
