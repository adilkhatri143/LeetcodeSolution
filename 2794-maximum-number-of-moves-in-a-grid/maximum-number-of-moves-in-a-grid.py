class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ans = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        max_ans = 0
        for col in range(len(grid[0]) - 2, -1, -1):
            for row in range(len(grid)):
                max_val = float("-inf")
                if row > 0 and grid[row][col] < grid[row - 1][col + 1]:
                    max_val = max(max_val, ans[row - 1][col + 1])
                if grid[row][col] < grid[row][col + 1]:
                    max_val = max(max_val, ans[row][col + 1])
                if row < len(grid) - 1 and grid[row][col] < grid[row + 1][col + 1]:
                    max_val = max(max_val, ans[row + 1][col + 1])
                ans[row][col] = 0 if max_val == float("-inf") else 1 + max_val
                if col == 0:
                    max_ans = max(max_ans, ans[row][col])
        return max_ans