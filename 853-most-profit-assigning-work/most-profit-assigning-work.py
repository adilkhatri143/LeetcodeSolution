import heapq
class Solution:
    class Pair:
        def __init__(self, d, p):
            self.d = d
            self.p = p
        
        def __lt__(self, obj):
            return self.p < obj.p
        
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        heap = []
        for d, p in zip(difficulty, profit):
            heapq.heappush(heap, self.Pair(d,-p))
        worker.sort(reverse=True)
        total_profit = 0
        for emp in worker:
            while heap and heap[0].d > emp:
                heapq.heappop(heap)
            if not heap:
                return total_profit
            total_profit += -heap[0].p
        return total_profit
