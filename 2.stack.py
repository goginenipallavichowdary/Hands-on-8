class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [0] * capacity  # Simulating C-style array
        self.top = -1

    def push(self, item):
        if self.is_full():
            raise Exception("Stack overflow")
        self.top += 1
        self.array[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        item = self.array[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.array[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

# Example usage and output
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack size:", stack.size())
print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("New top element:", stack.peek())
print("Stack size after pop:", stack.size())

#output:
#Stack size: 3
#Top element: 30
#Popped: 30
#New top element: 20
#Stack size after pop: 2
