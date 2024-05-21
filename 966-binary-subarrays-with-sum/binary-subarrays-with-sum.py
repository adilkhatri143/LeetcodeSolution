class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ht = dict()
        ht[0] = 1
        cur_sum = max_subarray = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - goal in ht:
                max_subarray += ht[cur_sum - goal]
            if cur_sum in ht:
                ht[cur_sum] += 1
            else:
                ht[cur_sum] = 1
        return max_subarray

