class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_freq = float("-inf")
        num_to_freq = Counter(nums)
        max_freq = max(num_to_freq.values())
        num_to_freq.clear()
        window_end = 0
        res = float("inf")
        for window_start in range(len(nums)):
            num_to_freq[nums[window_start]] = num_to_freq.get(nums[window_start], 0) + 1
            while num_to_freq[nums[window_start]] == max_freq:
                res = min(res, window_start - window_end + 1)
                num_to_freq[nums[window_end]] = num_to_freq.get(nums[window_end]) - 1
                window_end += 1
        return res
