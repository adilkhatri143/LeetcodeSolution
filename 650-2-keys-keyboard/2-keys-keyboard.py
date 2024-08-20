class Solution:
    def solve(self, chars, steps, prev, n):
        if chars == n:
            return steps
        if chars > n:
            return float("inf")
        cp_ans = self.solve(chars + chars, steps + 2, chars, n)
        p_ans = float("inf")
        if chars != 1:
            p_ans = self.solve(chars + prev, steps + 1, prev, n)
        return min(cp_ans, p_ans)


    def minSteps(self, n: int) -> int:
        return self.solve(1, 0, 0, n)