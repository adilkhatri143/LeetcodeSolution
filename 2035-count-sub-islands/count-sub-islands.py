class Solution:
    def solve(self, row, col, grid1, grid2):
        answer = True
        if grid1[row][col] == 0:
            answer = False
        grid2[row][col] = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for x, y in directions:
            new_row = row + x
            new_col = col + y
            if 0 <= new_row < len(grid1) and 0 <= new_col < len(grid1[0]) and grid2[new_row][new_col] == 1:
                answer = self.solve(new_row, new_col, grid1, grid2) and answer 
        return answer


    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        res = 0
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1 and self.solve(row, col, grid1, grid2):
                    res += 1
        return res