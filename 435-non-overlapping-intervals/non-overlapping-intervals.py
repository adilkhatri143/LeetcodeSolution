class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        stack = list()
        count = 0
        for s, e in intervals:
            if stack and (s < stack[-1] or e < stack[-1]):
                count += 1
            else:
                stack.append(e)
        return count