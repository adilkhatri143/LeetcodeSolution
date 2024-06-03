class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx_t = idx_s = 0
        while idx_s < len(s):
            if idx_t < len(t) and s[idx_s] == t[idx_t]:
                idx_t += 1
            idx_s += 1
        return len(t) - idx_t