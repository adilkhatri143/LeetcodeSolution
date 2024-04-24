class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        first, second, third = 0, 1, 1
        for i in range(3, n + 1):
            total = first + second + third
            first = second
            second = third
            third = total
        return third
