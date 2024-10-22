# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        max_heap = []
        q.append(root)
        while q:
            size = len(q)
            temp_sum = 0
            while size:
                node = q.popleft()
                temp_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1
            heapq.heappush(max_heap, -temp_sum)
        for i in range(k - 1):
            if len(max_heap):
                heapq.heappop(max_heap)
            else:
                return -1
        return -heapq.heappop(max_heap) if len(max_heap) else -1
        
