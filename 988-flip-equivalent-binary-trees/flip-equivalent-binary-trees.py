# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return (
                (self.solve(root1.left, root2.left) and self.solve(root1.right, root2.right)) or
                (self.solve(root1.left, root2.right) and self.solve(root1.right, root2.left))
            )
        return False

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.solve(root1, root2)