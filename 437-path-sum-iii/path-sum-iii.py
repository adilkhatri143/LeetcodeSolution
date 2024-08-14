# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def find_sum(self, csum, root, target_sum):
        if root is None:
            return 0
        
        csum += root.val
        if csum == target_sum:
            self.answer += 1
        self.find_sum(csum, root.left, target_sum)
        self.find_sum(csum, root.right, target_sum)
    
    def solve(self, root, target_sum):
        if root is None:
            return 0

        self.find_sum(0, root, target_sum)
        self.solve(root.left, target_sum)
        self.solve(root.right, target_sum)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.answer = 0
        self.solve(root, targetSum)
        return self.answer