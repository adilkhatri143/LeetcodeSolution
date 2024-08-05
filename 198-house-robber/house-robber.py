class Solution:
    def solve(self, idx, nums, dp):
        if idx >= len(nums):
            return 0
        if dp[idx] != float('-inf'):
            return dp[idx]
        dp[idx] = max(nums[idx] + self.solve(idx + 2, nums, dp), self.solve(idx + 1, nums, dp))
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        dp = [float('-inf') for i in range(len(nums))]
        return self.solve(0, nums, dp)