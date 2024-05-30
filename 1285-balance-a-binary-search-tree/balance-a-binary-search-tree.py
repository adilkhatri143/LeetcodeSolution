# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_list = list()
        def dfs(root):
            nonlocal node_list
            if root is None: return None
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)
        dfs(root)

        def build(l, r):
            nonlocal node_list
            if l <= r:
                mid = (l + r) // 2
                new_node = TreeNode(node_list[mid])
                new_node.left, new_node.right = build(l, mid - 1), build(mid + 1, r)
                return new_node
            return None
        return build(0, len(node_list) - 1)