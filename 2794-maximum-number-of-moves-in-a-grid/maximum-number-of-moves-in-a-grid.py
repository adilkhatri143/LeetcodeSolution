class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        prev = [0 for j in range(len(grid))]
        max_ans = 0
        for col in range(len(grid[0]) - 2, -1, -1):
            current = [0 for j in range(len(grid))]
            for row in range(len(grid)):
                max_val = float("-inf")
                if row > 0 and grid[row][col] < grid[row - 1][col + 1]:
                    max_val = max(max_val, prev[row - 1])
                if grid[row][col] < grid[row][col + 1]:
                    max_val = max(max_val, prev[row])
                if row < len(grid) - 1 and grid[row][col] < grid[row + 1][col + 1]:
                    max_val = max(max_val, prev[row + 1])
                current[row] = 0 if max_val == float("-inf") else 1 + max_val
            prev = current
        return max(prev)