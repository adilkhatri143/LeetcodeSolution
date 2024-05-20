class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if min(nums) != 0:
            return len(nums) - 1
        max_len = window_end = count_one = 0
        for window_start in range(len(nums)):
            if nums[window_start] == 1:
                count_one += 1
            if window_start - window_end + 1 - count_one > 1:
                max_len = max(max_len, window_start - window_end - 1)
                if nums[window_end] == 1:
                    count_one -= 1
                window_end += 1
        return max(max_len, window_start - window_end)