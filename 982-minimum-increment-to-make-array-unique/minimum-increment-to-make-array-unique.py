class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        minimum_increment = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                add_to_current_num = nums[i - 1] - nums[i] + 1
                nums[i] = add_to_current_num + nums[i]
                minimum_increment += add_to_current_num
        return minimum_increment