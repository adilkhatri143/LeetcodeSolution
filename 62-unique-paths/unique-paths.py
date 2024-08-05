class Solution:
    def solve(self, cur_row, cur_col, rows, cols, dp):
        if cur_row >= rows or cur_col >= cols:
            return 0
        if cur_row == rows - 1 and cur_col == cols - 1:
            return 1
        if dp[cur_row][cur_col] != -1:
            return dp[cur_row][cur_col]
        dp[cur_row][cur_col] = self.solve(cur_row + 1, cur_col, rows, cols, dp) + self.solve(cur_row, cur_col + 1, rows, cols, dp)
        return dp[cur_row][cur_col]
    

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        return self.solve(0, 0, m, n, dp)