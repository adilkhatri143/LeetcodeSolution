class Solution:

    def solve(self, word1, word2, m, n, dp):
        if m == 0:
            return n
        if n == 0:
            return m
        if m == 0 and n == 0:
            return float('inf')
        
        if dp[m - 1][n - 1] != float('inf'):
            return dp[m - 1][n - 1]

        if word1[m - 1] != word2[n - 1]:
            dp[m - 1][n - 1] = 1 + min(
                self.solve(word1, word2, m - 1, n, dp),
                self.solve(word1, word2, m - 1, n - 1, dp),
                self.solve(word1, word2, m, n - 1, dp)
            )
        else:
            dp[m - 1][n - 1] = self.solve(word1, word2, m - 1, n - 1, dp)
        return dp[m - 1][n - 1]

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[float('inf') for i in range(n)] for j in range(m)]
        return self.solve(word1, word2, m, n, dp)