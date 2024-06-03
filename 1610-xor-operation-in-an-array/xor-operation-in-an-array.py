class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(start, start + n):
            result ^= (start + (2 * (i - start)))
        return result