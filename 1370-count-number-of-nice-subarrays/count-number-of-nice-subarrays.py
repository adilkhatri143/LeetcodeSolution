class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def extactlyK(t):
            window_start = window_end = answer = 0
            while window_start < len(nums):
                t -= nums[window_start] % 2
                while window_end <= window_start and t < 0:
                    t += nums[window_end] % 2
                    window_end += 1
                answer += (window_start - window_end + 1)
                window_start += 1
            return answer
        
        return extactlyK(k) - extactlyK(k - 1)