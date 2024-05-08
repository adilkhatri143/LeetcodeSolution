"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        ht = dict()
        cur = head
        while cur:
            ht[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            node = ht.get(cur)
            if cur.next:
                node.next = ht[cur.next]
            if cur.random:
                node.random = ht[cur.random]
            cur = cur.next
        return ht[head]
        