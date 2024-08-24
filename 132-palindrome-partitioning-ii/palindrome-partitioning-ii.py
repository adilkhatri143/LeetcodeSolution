class Solution:
    def solve(self, idx, s, dp):
        if idx == len(s):
            return 0
        if idx in dp:
            return dp[idx]
        minimum_cuts = float("inf")
        for i in range(idx, len(s)):
            if s[idx: i + 1] == s[idx: i + 1][::-1]:
                minimum_cuts = min(minimum_cuts, 1 + self.solve(i + 1, s, dp))
        dp[idx] = minimum_cuts
        return dp[idx]

    def minCut(self, s: str) -> int:
        return self.solve(0, s, dict()) - 1