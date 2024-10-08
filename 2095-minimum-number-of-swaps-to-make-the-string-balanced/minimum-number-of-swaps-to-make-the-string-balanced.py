class Solution:
    def minSwaps(self, s: str) -> int:
        opening_bracket_count = 0
        for ch in s:
            if ch == "[":
                opening_bracket_count += 1
            else:
                if opening_bracket_count > 0:
                    opening_bracket_count -= 1
        return (opening_bracket_count + 1) // 2