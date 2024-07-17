# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, root, value, path):
        if root is None: return False
        if root.val == value:
            return True
        path.append("L")
        if self.find_path(root.left, value, path):
            return True
        path.pop()
        path.append("R")
        if self.find_path(root.right, value, path):
            return True
        path.pop()
        return False

    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        left_path = []
        right_path = []
        self.find_path(root, startValue, left_path)
        self.find_path(root, destValue, right_path)
        print(left_path)
        print(right_path)
        i = j = 0
        while i < len(left_path) and j < len(right_path) and left_path[i] == right_path[j]:
            i += 1
            j += 1
        
        for k in range(i, len(left_path)):
            left_path[k] = "U"
        return "".join(left_path[i:]) + "".join(right_path[j:])