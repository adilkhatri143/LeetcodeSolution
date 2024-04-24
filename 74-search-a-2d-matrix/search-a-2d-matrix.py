class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        low = 0
        high = rows * columns - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // columns][mid % columns] == target:
                return True
            elif matrix[mid // columns][mid % columns] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        
