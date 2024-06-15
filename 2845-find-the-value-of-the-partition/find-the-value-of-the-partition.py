class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        minimum = float('inf')
        for i in range(1, len(nums)):
            minimum = min(minimum, abs(nums[i - 1] - nums[i]))
        return minimum

