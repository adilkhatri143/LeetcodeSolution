class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_to_idx = dict()
        cur_sum = 0
        sum_to_idx[0] = -1
        for idx, num in enumerate(nums):
            cur_sum += num
            rem = cur_sum % k
            if rem in sum_to_idx and idx - sum_to_idx[rem] >= 2:
                return True
            if rem not in sum_to_idx:
                sum_to_idx[rem] = idx
        return False
            