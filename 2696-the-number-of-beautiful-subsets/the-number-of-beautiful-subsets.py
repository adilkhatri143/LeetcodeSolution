class Solution:
    def solve(self, idx, nums, exists, k):
        if idx == len(nums):
            return 1
        pick_answer = 0
        if nums[idx] - k not in exists and nums[idx] + k not in exists:
            exists[nums[idx]] = exists.get(nums[idx], 0) + 1
            pick_answer = self.solve(idx + 1, nums, exists, k)
            exists[nums[idx]] -= 1
            if exists[nums[idx]] == 0:
                exists.pop(nums[idx])
        not_pick_answer = self.solve(idx + 1, nums, exists, k)
        return pick_answer + not_pick_answer

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        return self.solve(0, nums, dict(), k) - 1