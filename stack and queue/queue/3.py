class RecentCounter:
    def __init__(self):
        self.q = []

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.pop(0)
        return len(self.q)

recent_counter = RecentCounter()
print(recent_counter.ping(1))
print(recent_counter.ping(100))
print(recent_counter.ping(3001))
print(recent_counter.ping(3002))