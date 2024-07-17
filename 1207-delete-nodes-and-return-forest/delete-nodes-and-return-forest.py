# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    forest = dict()
    def find_nodes(self, root, to_delete):
        if root is None: return root
        self.find_nodes(root.left, to_delete)
        if root.left and root.left.val in to_delete:
            if root.left.left:
                self.forest[root.left.left.val] = root.left.left
                root.left.left = None
            if root.left.right:
                self.forest[root.left.right.val] = root.left.right
                root.left.right = None
            root.left = None
        self.find_nodes(root.right, to_delete)
        if root.right and root.right.val in to_delete:
            if root.right.left:
                self.forest[root.right.left.val] = root.right.left
                root.right.left = None
            if root.right.right:
                self.forest[root.right.right.val] = root.right.right
                root.right.right = None
            root.right = None
        

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.forest = dict()
        to_delete = set(to_delete)
        self.find_nodes(root, to_delete)
        if root.val in to_delete:
            if root.left:
                self.forest[root.left.val] = root.left
                root.left = None
            if root.right:
                self.forest[root.right.val] = root.right
                root.right = None
        else:
            self.forest[root.val] = root
        return list(self.forest.values())