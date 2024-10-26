# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cur_max_height = 0
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_to_height = dict()
        def traverse_left_to_right(root, cur_height):
            nonlocal node_to_height
            if root is None:
                return
            node_to_height[root.val] = self.cur_max_height
            self.cur_max_height = max(cur_height, self.cur_max_height)
            traverse_left_to_right(root.left, cur_height + 1)
            traverse_left_to_right(root.right, cur_height + 1)
        
        def traverse_right_to_left(root, cur_height):
            nonlocal node_to_height
            if root is None:
                return
            node_to_height[root.val] = max(node_to_height[root.val], self.cur_max_height)
            self.cur_max_height = max(self.cur_max_height, cur_height)
            traverse_right_to_left(root.right, cur_height + 1)
            traverse_right_to_left(root.left, cur_height + 1)
        
        traverse_left_to_right(root, 0)
        self.cur_max_height = 0
        traverse_right_to_left(root, 0)
        return [node_to_height[val] for val in queries]

