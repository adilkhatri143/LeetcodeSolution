class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append([val, min(val, self.stack[-1][1])])
            return
        self.stack.append([val, val])

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()[0]
        return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()