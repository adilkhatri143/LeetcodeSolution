# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next.next is None:
            return [-1, -1]
        min_idx = max_idx = prev_max_idx = 2
        cur_idx = 2
        minf = maxf = True
        min_dis = float('inf')
        prev_node = head
        itr_node = head.next
        while itr_node.next:
            if prev_node.val < itr_node.val > itr_node.next.val:
                if min_idx == 2 and minf:
                    min_idx = cur_idx
                    minf = False
                if max_idx == 2 and maxf:
                    max_idx = cur_idx
                    prev_max_idx = max_idx
                    maxf = False
                else:
                    min_dis = min(min_dis, cur_idx - max_idx)
                    prev_max_idx = max_idx
                    max_idx = cur_idx
            elif prev_node.val > itr_node.val < itr_node.next.val:
                if min_idx == 2 and minf:
                    min_idx = cur_idx
                    minf = False
                if max_idx == 2 and maxf:
                    max_idx = cur_idx
                    prev_max_idx = max_idx
                    maxf = False
                else:
                    min_dis = min(min_dis, cur_idx - max_idx)
                    prev_max_idx = max_idx
                    max_idx = cur_idx
            cur_idx += 1
            prev_node = itr_node
            itr_node = itr_node.next
        print(min_dis, max_idx, min_idx)
        return [
            min_dis if min_dis != float('inf') else -1,
            max_idx - min_idx if max_idx - min_idx != 0 else -1
        ]