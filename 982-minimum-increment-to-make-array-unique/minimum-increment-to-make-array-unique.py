class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_element = max(nums)
        count_arr = [0] * (max_element + len(nums) + 1)
        min_increment = 0
        for i in range(len(nums)):
            count_arr[nums[i]] += 1
        for i in range(len(count_arr) - 1):
            if count_arr[i] != 0 and count_arr[i] != 1:
                extra = count_arr[i] - 1
                min_increment += extra
                count_arr[i + 1] += extra
        return min_increment