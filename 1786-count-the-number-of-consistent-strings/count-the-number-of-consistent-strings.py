class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_char = set(allowed)
        res = 0
        for word in words:
            for ch in word:
                if ch not in allowed_char:
                    break
            else:
                res += 1
        return res