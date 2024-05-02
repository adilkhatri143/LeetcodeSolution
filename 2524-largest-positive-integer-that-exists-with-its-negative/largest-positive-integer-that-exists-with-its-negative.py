class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_num = -1
        for num in nums:
            if num > 0 and -num in nums_set:
                max_num = max(max_num, num)
        return max_num
