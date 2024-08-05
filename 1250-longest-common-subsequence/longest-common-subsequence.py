class Solution:
    def solve(self, text1, text2, m, n, dp):
        if m == 0 or n == 0:
            return 0
        
        if (m - 1, n - 1) in dp:
            return dp[(m -1, n - 1)]

        if text1[m - 1] == text2[n - 1]:
            dp[(m -1, n - 1)] = 1 + self.solve(text1, text2, m - 1, n - 1, dp)
        else:
            dp[(m -1, n - 1)] = max(self.solve(text1, text2, m - 1, n, dp), self.solve(text1, text2, m, n - 1, dp))
        return dp[(m -1, n - 1)]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1, text2, len(text1), len(text2), dict())