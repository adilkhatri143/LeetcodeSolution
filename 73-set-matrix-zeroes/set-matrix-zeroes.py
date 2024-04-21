class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
                    if row == 0:
                        first_row_zero = True
                    if col == 0:
                        first_col_zero = True
        
        for row in range(1, rows):
            for col in range(1, cols):
                matrix[row][col] = 0 if matrix[row][0] == 0 or matrix[0][col] == 0 else matrix[row][col]
        
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0

        return matrix