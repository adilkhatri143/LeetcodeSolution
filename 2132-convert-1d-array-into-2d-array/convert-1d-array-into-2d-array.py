class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        result = [[0 for i in range(n)] for j in range(m)]
        idx = 0
        for r in range(m):
            for c in range(n):
                result[r][c] = original[idx]
                idx += 1
        return result
