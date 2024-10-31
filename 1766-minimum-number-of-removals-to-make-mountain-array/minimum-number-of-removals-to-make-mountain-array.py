class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n
        for i in range(1, n):
            max_inc = 0
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    max_inc = max(max_inc, lis[j])
            lis[i] = 1 + max_inc
        lds = [1] * n
        for i in range(n - 2, -1, -1):
            max_inc = 0
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    max_inc = max(max_inc, lds[j])
            lds[i] = 1 + max_inc
            min_remove = float("inf")
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:
                min_remove = min(min_remove, n - (lis[i] + lds[i] - 1))
        return min_remove