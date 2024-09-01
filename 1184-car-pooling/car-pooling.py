class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        total = [0] * 1002
        max_to = float("-inf")
        for pas, fr, to in trips:
            total[fr] += pas
            total[to] -= pas
            max_to = max(max_to, to)
        for i in range(max_to + 1):
            if i != 0:
                total[i] = total[i - 1] + total[i]
            if total[i] > capacity:
                return False
        return True