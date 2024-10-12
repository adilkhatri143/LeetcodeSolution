class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        leaving = []
        ans = 0
        for arr, dep in intervals:
            while leaving and arr > leaving[0]:
                heapq.heappop(leaving)
            heapq.heappush(leaving, dep)
            ans = max(ans, len(leaving))
        return ans