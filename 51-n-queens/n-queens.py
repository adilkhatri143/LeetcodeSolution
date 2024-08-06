class Solution:
    answer = list()
    def can_be_placed(self, board, row, col, n):
        for i in range(row - 1, -1, -1):
            if board[i][col] == "Q":
                return False
            
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        r = row - 1
        c = col + 1
        while r >= 0 and c < len(board[0]):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        
        return True

    def solve(self, board, row, n):
        if row == n:
            # append answer ro list
            self.answer.append(["".join(board[r]) for r in range(n)])
            return
        
        for col in range(n):
            if self.can_be_placed(board, row, col, n):
                board[row][col] = "Q"
                self.solve(board, row + 1, n)
                board[row][col] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.answer = list()
        board = [["." for i in range(n)] for j in range(n)]
        self.solve(board, 0, n)
        return self.answer