class Solution:
    count = 0
    def solve(self, grid, row, col, empty_sq):
        if grid[row][col] == 2 and empty_sq == -1:
            self.count += 1
            return
        elif grid[row][col] == 2:
            return 

        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for x, y in direction:
            new_row = row + x
            new_col = col + y
            if 0 <= new_row <= len(grid) - 1 and 0 <= new_col <= len(grid[0]) - 1 and grid[new_row][new_col] != -1:
                og = grid[row][col]
                grid[row][col] = -1
                empty_sq -= 1
                self.solve(grid, new_row, new_col, empty_sq)
                grid[row][col] = og
                empty_sq += 1


    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count = 0
        start_row = -1
        start_col = -1
        empty_sq = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col
                if grid[row][col] == 0:
                    empty_sq += 1
        self.solve(grid, start_row, start_col, empty_sq)
        return self.count