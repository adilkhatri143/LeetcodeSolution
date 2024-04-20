class Solution:
    def solve(self, row, col, rows, cols, land):
        if row < 0 or row >= rows or col < 0 or col >= cols or land[row][col] == -1 or land[row][col] == 0:
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
                if land[row][col] == 1:
                    temp = [row, col]
                    end_boundary = self.solve(row, col, rows, cols, land)
                    temp.extend(end_boundary)
                    ans.append(temp)
        return ans
                