# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_of_a = 0
        len_of_b = 0
        cur = headA
        while cur:
            len_of_a += 1
            cur = cur.next
        cur = headB
        while cur:
            len_of_b += 1
            cur = cur.next
        cur_of_a = headA
        cur_of_b = headB
        if len_of_a > len_of_b:
            while cur_of_a:
                len_of_a -= 1
                cur_of_a = cur_of_a.next
                if len_of_a == len_of_b:
                    break
        elif len_of_a < len_of_b:
            while cur_of_b:
                len_of_b -= 1
                cur_of_b = cur_of_b.next
                if len_of_b == len_of_a:
                    break
        
        while cur_of_a and cur_of_b:
            if cur_of_a == cur_of_b:
                return cur_of_a
            cur_of_a = cur_of_a.next
            cur_of_b = cur_of_b.next
        return None
