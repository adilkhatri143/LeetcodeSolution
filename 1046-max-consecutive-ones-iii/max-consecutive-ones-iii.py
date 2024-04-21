class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        max_window = float('-inf')
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros == k + 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
            right += 1
        return max_window