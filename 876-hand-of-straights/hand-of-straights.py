import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        num_to_count = Counter(hand)
        heap = list(num_to_count.keys())
        heapq.heapify(heap)
        while heap:
            min_num = heap[0]
            for i in range(groupSize):
                if min_num + i not in num_to_count:
                    return False
                num_to_count[min_num + i] -= 1
                if num_to_count[min_num + i] == 0 and min_num + i != heapq.heappop(heap):
                    return False
        return True