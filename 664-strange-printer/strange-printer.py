class Solution:
    def solve(self, idx, n, s, dp):
        if idx == n:
            return 1
        if dp[idx][n] != float("inf"):
            return dp[idx][n]
        min_turns = float("inf")
        for i in range(idx, n):
            min_turns = min(min_turns, self.solve(idx, i, s, dp) + self.solve(i + 1, n, s, dp))
        dp[idx][n] = min_turns - 1 if s[idx] == s[n] else min_turns
        return dp[idx][n]

    def strangePrinter(self, s: str) -> int:
        dp = [[float("inf") for i in range(len(s))] for j in range(len(s))]
        return self.solve(0, len(s) - 1, s, dp)