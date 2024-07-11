class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        for ch in s:
            if ")" in ch:
                data = list()
                while stack and stack[-1] != "(":
                    data.append(stack.pop())
                stack.pop()
                for ch in data:
                    stack.append(ch)
            else:
                stack.append(ch)
        return "".join(stack)

            