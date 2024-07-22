class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            left[i] = left[i] * right
            right *= nums[i]
        return left