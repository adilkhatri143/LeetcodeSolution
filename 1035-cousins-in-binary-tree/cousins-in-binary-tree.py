# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def bfs(self, root, val):
        level = 0
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            while size:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if node.left.val == val:
                        return level + 1, node
                if node.right:
                    q.append(node.right)
                    if node.right.val == val:
                        return level + 1, node
                size -= 1
            level += 1
        return -1, TreeNode()
                

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_level, x_node = self.bfs(root, x)
        y_level, y_node = self.bfs(root, y)
        return x_level == y_level and x_node != y_node