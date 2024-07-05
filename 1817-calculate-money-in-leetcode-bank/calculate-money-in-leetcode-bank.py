class Solution:
    def totalMoney(self, n: int) -> int:
        quo = n // 7
        rem = n % 7
        total = 28 * quo
        for i in range(quo):
            total += (7 * i)
        for i in range(1, rem + 1):
            total += (i + quo)
        return total