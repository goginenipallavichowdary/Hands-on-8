class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = [-1] * capacity
        self.start = 0
        self.end = 0

    def enqueue(self, value):
        if self.end == self.capacity:
            print("Queue is full")
        else:
            self.elements[self.end] = value
            self.end += 1

    def dequeue(self):
        if self.start == self.end:
            print("Queue is empty")
        else:
            value = self.elements[self.start]
            self.start += 1
            return value

# Example 
capacity = int(input("Enter the size of the queue: "))
queue = Queue(capacity)
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())

"""output
Enter the size of the queue: 2
1"""
