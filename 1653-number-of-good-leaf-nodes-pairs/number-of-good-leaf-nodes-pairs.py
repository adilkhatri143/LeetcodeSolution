# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def makeGraph(self, root, prev, graph, leaves):
        if root is None:
            return root
        if root.left is None and root.right is None:
            leaves.add(root)
        
        if prev is not None:
            graph[root].append(prev)
            graph[prev].append(root)
        
        self.makeGraph(root.left, root, graph, leaves)
        self.makeGraph(root.right, root, graph, leaves)
        
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = defaultdict(list)
        leaves = set()
        self.makeGraph(root, None, graph, leaves)
        count = 0
        for leaf in leaves:
            que = deque()
            visited = set()
            que.append(leaf)
            visited.add(leaf)
            for i in range(distance + 1):
                size = len(que)
                while size:
                    node = que.popleft()
                    if node != leaf and node in leaves:
                        count += 1
                    for nbr in graph[node]:
                        if nbr not in visited:
                            que.append(nbr)
                            visited.add(nbr)
                    size -= 1
        return count // 2