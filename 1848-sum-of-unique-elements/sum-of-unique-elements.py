class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_to_freq = Counter(nums)
        return sum(k if v == 1 else 0 for k, v in num_to_freq.items())