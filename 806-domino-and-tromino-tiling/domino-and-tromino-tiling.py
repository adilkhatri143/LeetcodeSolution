class Solution:
    def numTilings(self, n: int) -> int:
        prev_full, full, top_empty, bottom_empty = 1, 1, 0, 0
        for i in range(2, n + 1):
            new_full = full + prev_full + top_empty + bottom_empty
            top_empty = top_empty + prev_full
            bottom_empty = bottom_empty + prev_full
            prev_full = full
            full = new_full
        return full % (10 ** 9 + 7)