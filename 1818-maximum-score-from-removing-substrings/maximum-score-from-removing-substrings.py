class Solution:
    def solve(self, s, a, b, x, y, grt):
        stack = list()
        total = 0
        for ch in s:
            if stack and stack[-1] == a and ch == b:
                stack.pop()
                total += x if grt else y
            else:
                stack.append(ch)
        s = "".join(stack)
        stack.clear()
        for ch in s:
            if stack and stack[-1] == b and ch == a:
                stack.pop()
                total += y if grt else x
            else:
                stack.append(ch)
        return total
        
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            # ab will have high priority
            return self.solve(s, "a", "b", x, y, 1)
        else:
            # ba will have high priority
            return self.solve(s, "b", "a", x, y, 0)