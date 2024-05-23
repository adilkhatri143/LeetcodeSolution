class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        window_end = window_start = cur_sum = answer = 0
        while window_start < len(nums):
            cur_sum += nums[window_start]
            while cur_sum * (window_start - window_end + 1) >= k:
                cur_sum -= nums[window_end]
                window_end += 1
            answer += (window_start - window_end + 1)
            window_start += 1
        return answer


