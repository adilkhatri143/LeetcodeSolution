class StockSpanner:

    def __init__(self):
        self.stack = list()
        self.idx = 0

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack and price >= self.stack[-1][1]:
            self.stack.pop()
        top_idx = 0
        if self.stack:
            top_idx = self.stack[-1][0]
        self.stack.append((self.idx, price))
        return self.idx - top_idx
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)