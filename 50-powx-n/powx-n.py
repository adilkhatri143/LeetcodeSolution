class Solution:
    def solve(self, x, n):
        if n == 1:
            return x
        if n % 2 == 0:
            return self.solve(x * x, n // 2)
        else:
            return x * self.solve(x, n - 1)
    
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            return self.solve(x, n)
        elif n < 0:
            n = -n
            x = 1 / x
            return self.solve(x, n)
        return 1