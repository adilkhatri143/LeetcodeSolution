class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == "../":
                if count:
                    count = max(0, count - 1)
                continue
            if log == "./":
                continue
            count += 1
        return count