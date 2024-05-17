# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        if root is None:
            return root
        
        self.solve(root.left, target)
        self.solve(root.right, target)
        if root.left and root.left.val == -1:
            root.left = None
        if root.right and root.right.val == -1:
            root.right = None
        if root.left is None and root.right is None and root.val == target:
            root.val = -1

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.solve(root, target)
        if root.val == -1:
            return None
        return root