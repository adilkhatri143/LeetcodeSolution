# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        cur = head
        forw = head.next
        while cur:
            cur.next = prev
            prev = cur
            cur = forw if forw else None
            forw = forw.next if forw else None
        return prev
        
