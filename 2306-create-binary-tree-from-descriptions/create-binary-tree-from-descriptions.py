# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val_to_node = dict()
        for parent, child, is_left in descriptions:
            if parent not in val_to_node:
                val_to_node[parent] = TreeNode(parent)
            if child not in val_to_node:
                val_to_node[child] = TreeNode(child)
            node = val_to_node[parent]
            if is_left:
                node.left = val_to_node[child]
            else:
                node.right = val_to_node[child]
        for parent, child, is_left in descriptions:
            val_to_node.pop(child)
        return val_to_node.popitem()[1]