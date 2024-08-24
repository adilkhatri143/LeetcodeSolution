class Solution:
    def solve(self, start, arr, k, dp):
        if start == len(arr):
            return 0
        if start in dp:
            return dp[start]
        maximum_sum = float("-inf")
        cur_max = float("-inf")
        for i in range(start, min(start + k, len(arr))):
            cur_max = max(cur_max, arr[i])
            maximum_sum = max(maximum_sum, self.solve(i + 1, arr, k, dp) + cur_max * (i - start + 1))
        dp[start] = maximum_sum
        return dp[start]

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        return self.solve(0, arr, k, dict())