class Solution:
    def solve(self, row, col, rows, cols, land):
        if row >= rows or col >= cols or land[row][col] == -1 or land[row][col] == 0:
            return float('-inf'), float('-inf')
        land[row][col] = -1
        left_row, left_col = self.solve(row, col + 1, rows, cols, land)
        bottom_row, bottom_col = self.solve(row + 1, col, rows, cols, land)
        return [max(row, bottom_row), max(col, left_col)]
    
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        ans = list()
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1 and (row == 0 or land[row - 1][col] == 0) and (col == 0 or land[row][col - 1] == 0):
                    bottom_row = row
                    right_col = col
                    while bottom_row + 1 < rows and land[bottom_row + 1][col] == 1:
                        bottom_row += 1
                    while right_col + 1 < cols and land[row][right_col + 1] == 1:
                        right_col += 1
                    ans.append([row, col, bottom_row, right_col])
        return ans
                