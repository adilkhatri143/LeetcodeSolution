class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        result = ""
        for ch in s:
            if ch == "]":
                temp_str = ""
                while stack and stack[-1] != "[":
                    temp_str = stack.pop() + temp_str
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(temp_str * int(number))
            else:
                stack.append(ch)
        return "".join(stack)