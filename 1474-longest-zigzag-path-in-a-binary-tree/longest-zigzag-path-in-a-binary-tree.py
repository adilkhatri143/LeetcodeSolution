# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_len = 0
    class Pair():
        def __init__(self):
            self.left = -1
            self.right = -1
    
    def solve(self, root):
        if root is None:
            return self.Pair()
        
        left_node = self.solve(root.left)
        right_node = self.solve(root.right)

        new_pair = self.Pair()
        new_pair.left = left_node.right + 1
        new_pair.right = right_node.left + 1
        self.max_len = max(self.max_len, new_pair.left, new_pair.right)
        return new_pair
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        self.solve(root)
        return self.max_len