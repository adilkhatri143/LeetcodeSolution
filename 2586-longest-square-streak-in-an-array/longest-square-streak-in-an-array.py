class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        unique_num = set(nums)
        max_streak = 0
        for num in nums:
            current_num = num
            temp_streak =0
            while current_num in unique_num and current_num <= 10 ** 5:
                temp_streak += 1
                current_num *= current_num
            max_streak = max(max_streak, temp_streak)
        return max_streak if max_streak >= 2 else -1