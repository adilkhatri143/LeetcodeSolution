class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balanced = imbalanced = 0
        for ch in s:
            if ch == "(":
                balanced += 1
            else:
                if balanced > 0:
                    balanced -= 1
                else:
                    imbalanced += 1
        return balanced + imbalanced