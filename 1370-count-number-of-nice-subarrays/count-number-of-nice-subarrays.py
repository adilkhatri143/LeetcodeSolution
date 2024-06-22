class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def solve(nums, k):
            window_start = window_end = odd_count = answer = 0
            while window_start < len(nums):
                odd_count += nums[window_start] % 2
                while odd_count > k:
                    odd_count -= nums[window_end] % 2
                    window_end += 1
                answer += (window_start - window_end + 1)
                window_start += 1
            return answer

        return solve(nums, k) - solve(nums, k - 1)