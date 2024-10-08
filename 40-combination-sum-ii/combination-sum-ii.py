class Solution:
    answer = list()
    exist = set()
    def solve(self, candidates, idx, target, temp):
        if target == 0:
            joined_str = "".join(map(str, temp))
            if joined_str not in self.exist:
                self.exist.add(joined_str)
                self.answer.append(temp)
            return
        if idx == len(candidates):
            return

        if candidates[idx] <= target:
            self.solve(candidates, idx + 1, target - candidates[idx], temp + [candidates[idx]])
        
        # important step
        new_idx = idx + 1
        while new_idx < len(candidates) and candidates[new_idx] == candidates[idx]:
            new_idx += 1
        self.solve(candidates, new_idx, target, temp)
        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = list()
        self.exist = set()
        candidates.sort()
        self.solve(candidates, 0, target, [])
        return self.answer