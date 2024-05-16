# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root.left is None and root.right is None:
            return root.val
        left_ans = self.solve(root.left)
        right_ans = self.solve(root.right)
        if root.val == 2:
            return left_ans or right_ans
        return left_ans and right_ans

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None: return root
        return self.solve(root)