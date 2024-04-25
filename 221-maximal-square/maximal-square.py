class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            if int(matrix[i][-1]):
                ans = 1
                break

        for i in range(len(matrix[0])):
            if int(matrix[-1][i]):
                ans = 1
                break
                    
        for r in range(len(matrix) - 2, -1, -1):
            for c in range(len(matrix[0]) - 2, -1, -1):
                if int(matrix[r][c]) == 0: continue
                min_sq = min(int(matrix[r + 1][c]), int(matrix[r][c + 1]), int(matrix[r + 1][c + 1]))
                if min_sq:
                    matrix[r][c] = min_sq + 1
                ans = max(ans, int(matrix[r][c]))
        return ans * ans
                