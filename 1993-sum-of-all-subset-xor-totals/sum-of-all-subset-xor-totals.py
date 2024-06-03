class Solution:
    final_answer = 0
    def solve(self, idx, nums, temp_xor):
        if idx == len(nums):
            self.final_answer += temp_xor
            return
        
        self.solve(idx + 1, nums, temp_xor ^ nums[idx])
        self.solve(idx + 1, nums, temp_xor)

    def subsetXORSum(self, nums: List[int]) -> int:
        self.final_answer = 0
        self.solve(0, nums, 0)
        return self.final_answer