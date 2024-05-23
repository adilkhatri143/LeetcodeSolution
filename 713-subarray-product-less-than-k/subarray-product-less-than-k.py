class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        window_start = window_end = answer = 0
        cur_sum = 1
        while window_start < len(nums):
            cur_sum *= nums[window_start]
            while window_end <= window_start and cur_sum >= k:
                cur_sum //= nums[window_end]
                window_end += 1
            answer += (window_start - window_end + 1)
            window_start += 1
        return answer