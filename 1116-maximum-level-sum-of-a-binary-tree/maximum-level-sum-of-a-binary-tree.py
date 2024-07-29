# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        q = deque()
        q.append(root)
        max_level = max_sum = float('-inf')
        level = 1
        while q:
            size = len(q)
            total = 0
            while size:
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1
            if total > max_sum:
                max_sum = total
                max_level = level
            level += 1
        return max_level
            