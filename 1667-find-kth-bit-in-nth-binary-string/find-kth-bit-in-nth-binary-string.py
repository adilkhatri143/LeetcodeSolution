class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cur_s = [0]
        next_s = list()
        for i in range(2, n + 1):
            for i in range(len(cur_s)):
                next_s.append(cur_s[i])
            next_s.append(1)
            for i in range(len(cur_s) - 1, -1, -1):
                next_s.append(1 - cur_s[i])
            cur_s = next_s
            next_s = list()
        return str(cur_s[k - 1])
