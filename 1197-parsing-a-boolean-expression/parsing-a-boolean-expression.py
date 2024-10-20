class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = list()
        count_of_f = 0
        count_of_t = 0
        for ch in expression:
            if ch == ",":
                continue
            elif ch == ")":
                while stack and stack[-1] != "(":
                    if stack[-1] == "t":
                        count_of_t += 1
                    elif stack[-1] == "f":
                        count_of_f += 1
                    stack.pop()
                stack.pop()
                operator = stack.pop()
                if operator == "|":
                    if count_of_t >= 1:
                        stack.append("t")
                    else:
                        stack.append("f")
                elif operator == "&":
                    if count_of_f >= 1:
                        stack.append("f")
                    else:
                        stack.append("t")
                elif operator == "!":
                    if count_of_t >= 1:
                        stack.append("f")
                    else:
                        stack.append("t")
                count_of_f = 0
                count_of_t = 0
            else:
                stack.append(ch)
        final_val = stack.pop()
        return True if final_val == "t" else False