class Solution:
    answer = 0
    def solve(self, grid, row, col, rows, cols, max_val):
        if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] == 0 or grid[row][col] == -1:
            return 0

        original_value = grid[row][col]
        grid[row][col] = -1
        cur_max_value = max_val + original_value
        self.answer = max(self.answer, cur_max_value)
        self.solve(grid, row + 1, col, rows, cols, cur_max_value)
        self.solve(grid, row - 1, col, rows, cols, cur_max_value)
        self.solve(grid, row, col + 1, rows, cols, cur_max_value)
        self.solve(grid, row, col - 1, rows, cols, cur_max_value)
        grid[row][col] = original_value
 
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.answer = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    self.solve(grid, row, col, rows, cols, 0)
        return self.answer