class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        row_max = float('-inf')
        for r in range(n):
            cur_min = min(matrix[r])
            row_max = max(row_max, cur_min)
        
        col_min = float('inf')
        for c in range(m):
            cur_max = float('-inf')
            for r in range(n):
                cur_max = max(cur_max, matrix[r][c])
            col_min = min(col_min, cur_max)
        
        if row_max == col_min:
            return [row_max]
        return []