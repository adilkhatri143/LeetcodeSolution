class Solution:
    def minSwaps(self, s: str) -> int:
        stack = list()
        closing_bracket_count = 0
        for ch in s:
            if ch == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    closing_bracket_count += 1
            else:
                stack.append(ch)
        return (closing_bracket_count + 1) // 2