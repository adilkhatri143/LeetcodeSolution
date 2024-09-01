# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    answer = list()
    stack = list()
    def solve(self, head):
        if head.next is None:
            self.answer.append(0)
            self.stack.append(head.val)
            return
        self.solve(head.next)
        if head.val < self.stack[-1]:
            self.answer.append(self.stack[-1])
            self.stack.append(head.val)
        else:
            while self.stack and head.val >= self.stack[-1]:
                self.stack.pop()
            if self.stack:
                self.answer.append(self.stack[-1])
            else:
                self.answer.append(0)
            self.stack.append(head.val)


    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        self.answer = list()
        self.stack = list()
        self.solve(head)
        self.answer.reverse()
        return self.answer