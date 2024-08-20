class Solution:
    def solve(self, chars, prev, steps, n, dp):
        if chars == n:
            return steps
        if chars > n:
            return float("inf")
        if (chars, prev) in dp:
            return dp[(chars, prev)]
        cp_ans = self.solve(chars + chars, chars, steps + 2, n, dp)
        p_ans = float("inf")
        if chars != 1:
            p_ans = self.solve(chars + prev, prev, steps + 1, n, dp)
        dp[(chars, prev)] = min(cp_ans, p_ans)
        return dp[(chars, prev)]


    def minSteps(self, n: int) -> int:
        return self.solve(1, 1, 0, n, dict())