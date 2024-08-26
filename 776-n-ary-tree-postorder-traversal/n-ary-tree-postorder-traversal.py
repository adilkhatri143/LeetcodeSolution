"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    answer = list()
    def solve(self, root):
        if root is None:
            return 
        for child in root.children:
            self.solve(child)
        self.answer.append(root.val)
        
    def postorder(self, root: 'Node') -> List[int]:
        self.answer = list()
        self.solve(root)
        return self.answer