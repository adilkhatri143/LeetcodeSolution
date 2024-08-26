class Solution:
    def solve(self, idx, nums, dp):
        if idx >= len(nums):
            return 0
        if idx in dp:
            return dp[idx]
        cur_val = nums[idx]
        cur_sum = nums[idx]
        index = idx + 1
        next_idx_if_cur_num_not_pick = idx + 1
        while index < len(nums) and nums[index] == cur_val:
            cur_sum += nums[index]
            index += 1
            next_idx_if_cur_num_not_pick += 1
        
        while index < len(nums) and nums[index] == cur_val + 1:
            index += 1
        
        dp[idx] = max(cur_sum + self.solve(index, nums, dp), self.solve(next_idx_if_cur_num_not_pick, nums, dp))
        return dp[idx]

    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        return self.solve(0, nums, dict())