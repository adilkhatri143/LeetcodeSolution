# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    max_num = -1
    def solve(self, head):
        if head is None: return float("-inf")
        num = self.solve(head.next)
        self.max_num = max(self.max_num, num)
        if head.val < self.max_num:
            head.val = -1
        if head.next and head.next.val == -1:
            head.next = head.next.next
        return head.val


    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.max_num = -1
        self.solve(head)
        if head.next and head.next.val == -1:
            head.next = head.next
        if head and head.val == -1:
            return head.next
        return head