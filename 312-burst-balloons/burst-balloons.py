class Solution:
    def solve(self, start, end, nums, dp):
        if start > end: return 0
        if (start, end) in dp:
            return dp[(start, end)]
        maximum = float("-inf")
        for k in range(start, end + 1):
            coins = (nums[start - 1] * nums[k] * nums[end + 1]) + self.solve(start, k - 1, nums, dp) + self.solve(k + 1, end, nums, dp)
            maximum = max(maximum, coins)
        dp[(start, end)] = maximum
        return dp[(start, end)]

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        return self.solve(1, len(nums) - 2, nums, dict())