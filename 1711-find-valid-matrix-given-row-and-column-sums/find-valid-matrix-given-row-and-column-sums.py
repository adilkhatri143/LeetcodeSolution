class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        matrix = [[0 for i in range(m)] for j in range(n)]
        for r in range(n):
            for c in range(m):
                matrix[r][c] = min(rowSum[r], colSum[c])
                rowSum[r] -= matrix[r][c]
                colSum[c] -= matrix[r][c]
        return matrix