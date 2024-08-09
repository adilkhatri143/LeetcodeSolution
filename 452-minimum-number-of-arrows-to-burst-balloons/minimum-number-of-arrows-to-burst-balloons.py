class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        end = points[0][1]
        res = 1
        for s, e in points[1:]:
            if s > end:
                res += 1
                end = e
        return res