class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window_end = count = 0
        k = zero = 1
        for window_start in range(len(nums)):
            zero += (nums[window_start] - 1)
            while zero < 0:
                zero += (1 - nums[window_end])
                window_end += 1
            count = max(count, window_start - window_end + 1 - k)
        count = max(count, window_start - window_end + 1 - k)
        return count