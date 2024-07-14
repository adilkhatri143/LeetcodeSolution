class Solution:
    def getSmallestString(self, s: str) -> str:
        nums = list(map(int, s))
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == 0 and nums[i] % 2 == 0 and nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                break
            elif nums[i - 1] % 2 and nums[i] % 2 and nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                break
        return "".join(map(str, nums))