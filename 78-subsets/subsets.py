class Solution:
    answer = list()
    def solve(self, idx, nums, temp_answer):
        if idx == len(nums):
            self.answer.append(temp_answer)
            return

        self.solve(idx + 1, nums, temp_answer + [nums[idx]])
        self.solve(idx + 1, nums, temp_answer)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = list()
        self.solve(0, nums, [])
        return self.answer