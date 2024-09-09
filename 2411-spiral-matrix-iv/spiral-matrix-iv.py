# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for j in range(m)]
        itr = head
        left, right = 0, n
        top, bottom = 0, m
        while itr and left < right and top < bottom:
            for i in range(left, right):
                if itr is None: break
                matrix[top][i] = itr.val
                itr = itr.next
            top += 1

            for i in range(top, bottom):
                if itr is None: break
                matrix[i][right - 1] = itr.val
                itr = itr.next
            right -= 1

            for i in range(right - 1, left - 1, -1):
                if itr is None: break
                matrix[bottom - 1][i] = itr.val
                itr = itr.next
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                if itr is None: break
                matrix[i][left] = itr.val
                itr = itr.next
            left += 1
        
        return matrix