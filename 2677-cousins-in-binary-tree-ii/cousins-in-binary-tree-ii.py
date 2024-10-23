# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_to_sum = dict()
        q = deque()
        q.append(root)
        level = 0
        while q:
            size = len(q)
            sum_ = 0
            while size:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sum_ += node.val
                size -= 1
            level_to_sum[level] = sum_
            level += 1
        root.val = level = 0
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            while size:
                node = q.popleft()
                value_of_level = level_to_sum.get(level + 1, 0)
                right_val = node.right.val if node.right else 0
                left_val = node.left.val if node.left else 0
                if node.left:
                    q.append(node.left)
                    node.left.val = value_of_level - right_val - left_val
                if node.right:
                    q.append(node.right)
                    node.right.val = value_of_level - right_val - left_val
                size -= 1
            level += 1
        return root
        