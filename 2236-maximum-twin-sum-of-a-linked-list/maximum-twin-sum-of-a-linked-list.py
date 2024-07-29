# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid_node(self, head):
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_ll(self, head):
        if head.next is None:
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

    def find_max_sum(self, head, reverse_head):
        temp_head = head
        temp_rev_head = reverse_head
        max_sum = float('-inf')
        while temp_head:
            max_sum = max(max_sum, temp_head.val + temp_rev_head.val)
            temp_head = temp_head.next
            temp_rev_head = temp_rev_head.next
        return max_sum

    def pairSum(self, head: Optional[ListNode]) -> int:
        mid_node = self.find_mid_node(head)
        new_head = mid_node.next
        mid_node.next = None
        reverse_head = self.reverse_ll(new_head)
        return self.find_max_sum(head, reverse_head)
