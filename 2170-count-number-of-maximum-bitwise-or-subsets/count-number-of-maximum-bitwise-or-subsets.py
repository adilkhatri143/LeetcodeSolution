class Solution:
    or_to_count = dict()
    def solve(self, idx, nums, bor):
        if idx == len(nums):
            self.or_to_count[bor] = self.or_to_count.get(bor, 0) + 1
            return
        self.solve(idx + 1, nums, bor | nums[idx])
        self.solve(idx + 1, nums, bor)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.or_to_count.clear()
        self.solve(0, nums, 0)
        return self.or_to_count[max(self.or_to_count)]
