# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good_node = 0
    def solve(self, root, cur_max):
        if root is None: return 0
        if root.val >= cur_max:
            self.good_node += 1
        if root.left:
            self.solve(root.left, max(cur_max, root.left.val))
        if root.right:
            self.solve(root.right, max(cur_max, root.right.val))

    def goodNodes(self, root: TreeNode) -> int:
        self.good_node = 0
        if root is None: return self.good_node
        self.solve(root, root.val)
        return self.good_node