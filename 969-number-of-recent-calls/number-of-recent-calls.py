from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        if len(self.q) == 0:
            self.q.append(t)
            return len(self.q)
        if t - 3000 <= self.q[0] <= t:
            self.q.append(t)
            return len(self.q)
        while self.q:
            if t - 3000 > self.q[0]:
                self.q.popleft()
            elif t - 3000 <= self.q[0]:
                break
        self.q.append(t)
        return len(self.q)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)