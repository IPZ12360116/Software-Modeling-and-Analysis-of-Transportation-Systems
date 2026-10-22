class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop(0)

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
print(my_stack.top())
print(my_stack.pop())
print(my_stack.empty())