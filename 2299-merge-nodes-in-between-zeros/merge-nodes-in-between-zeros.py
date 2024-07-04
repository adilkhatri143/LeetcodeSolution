# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_head = None
        cur_head = head
        itr_head = head.next
        cur_sum = 0
        while itr_head:
            cur_sum += itr_head.val
            if itr_head.val == 0:
                prev_head = cur_head
                cur_head.val = cur_sum
                cur_head = cur_head.next
                cur_sum = 0
            itr_head = itr_head.next
        prev_head.next = None
        return head
