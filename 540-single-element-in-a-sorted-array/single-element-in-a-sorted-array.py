class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid + 1]:
                if (high - mid) % 2 == 0:
                    low = mid + 2
                else:
                    high = mid - 1
            else:
                if (high - mid) % 2 == 0:
                    if nums[mid] == nums[mid - 1]:
                        high = mid - 2
                    else:
                        return nums[mid]
                else:
                    low = mid + 1
        return nums[low]