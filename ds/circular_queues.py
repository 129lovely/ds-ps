class ArrayCircularQueue:
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.rear = -1
        self.front = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError("Queue full")

        self.rear = (self.rear + 1) if (self.rear + 1) < self.maxCount else -1
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue empty")

        self.front = (self.front + 1) if (self.front + 1) < self.maxCount else -1
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue empty")
        return self.data[(self.front + 1) if (self.front + 1) < self.maxCount else -1]