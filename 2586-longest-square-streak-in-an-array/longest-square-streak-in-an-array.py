class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        num_to_streak = dict()
        max_streak = 0
        for num in nums:
            root = int(math.sqrt(num))
            if root * root == num and root in num_to_streak:
                num_to_streak[num] = num_to_streak[root] + 1
            else:
                num_to_streak[num] = 1
            max_streak = max(max_streak, num_to_streak[num])
        return max_streak if max_streak >= 2 else -1