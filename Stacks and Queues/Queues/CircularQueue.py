from collections import deque


class CircularQueue:
    def __init__(self,capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.start = -1
        self.top = -1
        self.size = 0

    def __str__(self):
        values = [x for x in self.items]
        return ' '.join(values)

    def isFull(self):
        return self.capacity == self.size


    def isEmpty(self):
        return self.size == 0

    def enqueue(self,val):
        if self.isFull():
            print("que is full")
            return

        if self.isEmpty():
            self.top = 0
            self.start = 0
        else:
            self.top = (self.top + 1) % self.capacity

        self.items[self.top] = val
        self.size+=1

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        dequeued_val = self.items[self.start]
        self.size -=1
        self.top = (self.top +1) % self.capacity



queue = CircularQueue(5)
print(queue.items)  # Expected: [None, None, None, None, None]
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.items)  # Expected: [10, 20, 30, None, None]









