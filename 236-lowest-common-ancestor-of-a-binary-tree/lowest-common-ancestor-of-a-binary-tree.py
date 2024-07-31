# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        left_child = self.solve(root.left, p, q)
        right_child = self.solve(root.right, p, q)
        if left_child is None:
            return right_child
        elif right_child is None:
            return left_child
        else:
            return root
        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root, p, q)