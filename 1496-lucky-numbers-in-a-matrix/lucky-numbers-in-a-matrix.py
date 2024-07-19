class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        rowMin = set()
        for r in range(n):
            curMin = float('inf')
            for c in range(m):
                curMin = min(curMin, matrix[r][c])
            rowMin.add(curMin)
        colMax = set()
        for c in range(m):
            curMax = float('-inf')
            for r in range(n):
                curMax = max(curMax, matrix[r][c])
            colMax.add(curMax)
        answer = list()
        for val in rowMin:
            if val in colMax:
                answer.append(val)
        return answer