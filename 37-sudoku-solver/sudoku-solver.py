class Solution:
    def check_col(self, board, cur_row, cur_col, val):
        for i in range(9):
            if i == cur_row:
                continue
            if board[i][cur_col] == val:
                return False        
        return True
    
    def check_row(self, board, cur_row, cur_col, val):
        for i in range(9):
            if i == cur_col:
                continue
            if board[cur_row][i] == val:
                return False        
        return True
    
    def check_sub_matrix(self, board, cur_row, cur_col, val):
        start_row = cur_row // 3 * 3
        start_col = cur_col // 3 * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if i == cur_row and j == cur_col:
                    continue
                if board[i][j] == val:
                    return False
        return True
    
    def solve_sudoku(self, board, cur_row, cur_col):
        if cur_row == len(board):
            return True
        elif cur_col == len(board[0]):
            return self.solve_sudoku(board, cur_row + 1, 0) 
        elif board[cur_row][cur_col] != ".":
            return self.solve_sudoku(board, cur_row, cur_col + 1)
        
        for i in range(1, 10):
            val = str(i)
            if (
                self.check_row(board, cur_row, cur_col, val) and 
                self.check_col(board, cur_row, cur_col, val) and 
                self.check_sub_matrix(board, cur_row, cur_col, val)
            ):
                board[cur_row][cur_col] = val
                if self.solve_sudoku(board, cur_row, cur_col + 1):
                    return True
                board[cur_row][cur_col] = "."


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve_sudoku(board, 0, 0)
                    