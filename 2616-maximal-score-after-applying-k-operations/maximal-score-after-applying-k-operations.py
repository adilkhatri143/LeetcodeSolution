class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        ans = 0
        for num in nums:
            heapq.heappush(heap, -num)
        for i in range(k):
            val = - heapq.heappop(heap)
            ans += val
            heapq.heappush(heap, -ceil(val / 3))
        return ans