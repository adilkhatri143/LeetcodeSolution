class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maximum = [float("-inf") for i in range(len(nums))]
        maximum[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            maximum[i] = max(maximum[i + 1], nums[i])
        ans = i = j = 0
        while i < len(nums) and j < len(nums):
            if nums[i] <= maximum[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans