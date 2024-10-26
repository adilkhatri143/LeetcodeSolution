# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    node_to_height = dict()
    max_heights = dict()
    def find_max_height(self, root):
        if root is None:
            return -1

        if root.val in self.node_to_height:
            return self.node_to_height[root.val]

        cur_node_height = 1 + max(self.find_max_height(root.left), self.find_max_height(root.right))
        self.node_to_height[root.val] = cur_node_height
        return self.node_to_height[root.val]
    
    def solve(self, root, level, max_height):
        if root is None: return
        self.max_heights[root.val] = max_height
        self.solve(
            root.left,
            level + 1,
            max(max_height, level + 1 + self.find_max_height(root.right))
        )
        self.solve(
            root.right,
            level + 1,
            max(max_height, level + 1 + self.find_max_height(root.left))
        )

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.node_to_height.clear()
        self.max_heights.clear()
        self.solve(root, 0, 0)
        return [self.max_heights[val] for val in queries]