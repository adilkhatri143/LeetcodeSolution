class Solution:
    def countVowelStrings(self, n: int) -> int:
        prev = cur = [1, 1, 1, 1, 1]
        for i in range(1, n):
            cur[0] = prev[0] + prev[1] + prev[2] + prev[3] + prev[4]
            cur[1] = prev[1] + prev[2] + prev[3] + prev[4]
            cur[2] = prev[2] + prev[3] + prev[4]
            cur[3] = prev[3] + prev[4]
            cur[4] = prev[4]
            prev = cur
        return sum(cur)