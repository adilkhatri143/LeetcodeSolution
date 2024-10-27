class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if (row == m - 1 or col == n - 1) and matrix[row][col]:
                    ans += matrix[row][col]
                elif row != m - 1 and col != n - 1 and matrix[row][col]:
                    matrix[row][col] += min(matrix[row + 1][col], matrix[row][col + 1], matrix[row + 1][col + 1])
                    ans += matrix[row][col]
        return ans