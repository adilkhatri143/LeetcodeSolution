class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_char = set(allowed)
        res = 0
        for word in words:
            contains_char = set(word)
            diff = contains_char - allowed_char
            if len(diff) == 0:
                res += 1
        return res