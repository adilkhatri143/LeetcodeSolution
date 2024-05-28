class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        for x in range(max_num + 1):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            if count == x:
                return x
        return -1