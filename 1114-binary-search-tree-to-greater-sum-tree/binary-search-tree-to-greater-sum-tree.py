# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    def solve(self, root):
        if root is None: return 0
        self.solve(root.right)
        prev_val = 0 if not self.prev else self.prev.val
        root.val += prev_val
        self.prev = root
        self.solve(root.left)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.prev = None
        self.solve(root)
        return root
