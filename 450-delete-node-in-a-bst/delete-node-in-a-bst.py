# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_max(self, root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is not None and root.right is not None:
                temp = self.find_max(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
                return root
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                return None
        return root
        