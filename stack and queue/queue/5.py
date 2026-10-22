class MyCircularQueue:
    def __init__(self, k):
        self.k = k
        self.q = [0] * k
        self.head = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        idx = (self.head + self.size) % self.k
        self.q[idx] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        idx = (self.head + self.size - 1) % self.k
        return self.q[idx]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k

queue = MyCircularQueue(3)
print(queue.enQueue(1))
print(queue.enQueue(2))
print(queue.enQueue(3))
print(queue.enQueue(4))
print(queue.Rear())
print(queue.isFull())
print(queue.deQueue())
print(queue.enQueue(4))
print(queue.Rear())