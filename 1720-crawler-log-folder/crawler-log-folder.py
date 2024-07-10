class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = list()
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
                continue
            if log == "./":
                continue
            stack.append(log)
        return len(stack)