# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_ll(self, head):
        prev = None
        curr = head
        forw = head.next
        while curr:
            curr.next = prev
            prev = curr
            curr = forw
            forw = forw.next if forw else None
        
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return head
        mid = self.find_mid(head)
        second_head = mid.next
        mid.next = None
        reverse_second_head = self.reverse_ll(second_head)
        while head and reverse_second_head:
            if head.val == reverse_second_head.val:
                head = head.next
                reverse_second_head = reverse_second_head.next
            else:
                return False
        return True