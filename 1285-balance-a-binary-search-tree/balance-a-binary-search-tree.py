# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sort_list = []
        def inorder(root):
            nonlocal sort_list
            if root is None:
                return
            inorder(root.left)
            sort_list.append(root.val)
            inorder(root.right)
        inorder(root)

        def create_balance_tree(left, right):
            nonlocal sort_list
            if left > right:
                return None
            mid = (left + right) // 2
            new_node = TreeNode(sort_list[mid])
            new_node.left = create_balance_tree(left, mid - 1)
            new_node.right = create_balance_tree(mid + 1, right)
            return new_node 
        return create_balance_tree(0 , len(sort_list) - 1)