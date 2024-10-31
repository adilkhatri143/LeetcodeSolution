class Solution:
    def binary_search(self, lis, num):
        low, high = 0, len(lis)
        while low < high:
            mid = (low + high) // 2
            if lis[mid] < num:
                low = mid + 1
            else:
                high = mid
        return low
    
    def longest_increasing_subsequence(self, nums):
        lis_len = [1] * len(nums)
        lis = list()
        for i in range(len(nums)):
            idx = self.binary_search(lis, nums[i])
            if idx == len(lis):
                lis.append(nums[i])
            else:
                lis[idx] = nums[i]
            lis_len[i] = len(lis)
        return lis_len
    
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis = self.longest_increasing_subsequence(nums)
        nums.reverse()
        lds = self.longest_increasing_subsequence(nums)
        lds.reverse()
        min_removal = float("inf")
        for lis_val, lds_val in zip(lis, lds):
            if lis_val > 1 and lds_val > 1:
                min_removal = min(min_removal, len(nums) - (lis_val + lds_val - 1))
        return min_removal
