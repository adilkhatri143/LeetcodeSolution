class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last = cost[-1]
        second_last = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            og_second_last = second_last
            second_last = min(cost[i] + second_last, cost[i] + last)
            last = og_second_last
        return min(second_last, last)