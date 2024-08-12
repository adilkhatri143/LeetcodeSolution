class Solution:
    def numTilings(self, n: int) -> int:
        full, top_empty, bottom_empty = {0: 1, 1: 1}, {1: 0}, {1: 0}
        for i in range(2, n + 1):
            full[i] = full[i - 1] + full[i - 2] + top_empty[i - 1] + bottom_empty[i - 1]
            top_empty[i] = top_empty[i - 1] + full[i - 2]
            bottom_empty[i] = bottom_empty[i - 1] + full[i - 2]
        return full[n] % (10 ** 9 + 7)