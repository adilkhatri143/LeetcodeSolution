import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) == k + 1:
                heapq.heappop(heap)
        return heapq.heappop(heap)