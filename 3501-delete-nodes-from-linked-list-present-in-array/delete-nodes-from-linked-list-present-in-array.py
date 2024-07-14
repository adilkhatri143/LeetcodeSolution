# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if len(nums) == 0:
            return head
        nums_set = set(nums)
        new_head = ListNode(-1)
        new_head.next = head
        temp = new_head
        while temp.next:
            if temp.next.val in nums_set:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return new_head.next

    