class MyCircularDeque:
    def __init__(self, k):
        self.k = k
        self.q = [0] * k
        self.head = 0
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.k) % self.k
        self.q[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        idx = (self.head + self.size) % self.k
        self.q[idx] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def getRear(self):
        if self.isEmpty():
            return -1
        idx = (self.head + self.size - 1) % self.k
        return self.q[idx]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k

deque = MyCircularDeque(3)
print(deque.insertLast(1))
print(deque.insertLast(2))
print(deque.insertFront(3))
print(deque.insertFront(4))
print(deque.getRear())
print(deque.isFull())
print(deque.deleteLast())
print(deque.insertFront(4))
print(deque.getFront())