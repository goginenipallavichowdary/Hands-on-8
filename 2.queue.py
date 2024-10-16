class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [0] * capacity  # Simulating C-style array
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue overflow")
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue underflow")
        item = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def front_element(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.array[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_size(self):
        return self.size

# Example usage and output
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue size:", queue.get_size())
print("Front element:", queue.front_element())
print("Dequeued:", queue.dequeue())
print("New front element:", queue.front_element())
print("Queue size after dequeue:", queue.get_size())

#output:
#Queue size: 3
#Front element: 10
#Dequeued: 10
#New front element: 20
#Queue size after dequeue: 2
