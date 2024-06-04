import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        num_to_freq = dict()
        for num in arr:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1
        heap = []
        for num, occur in num_to_freq.items():
            freq = num_to_freq[num]
            heapq.heappush(heap, -freq)
        answer = 0
        total = 0
        while total < len(arr) / 2:
            answer += 1
            freq = -heapq.heappop(heap)
            total += freq
        return answer
        
        