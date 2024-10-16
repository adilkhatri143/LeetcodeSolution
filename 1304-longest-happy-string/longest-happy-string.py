class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))
        ans = []
        while heap:
            count, char = heapq.heappop(heap)
            count = -count
            if (
                len(ans) >= 2 and
                ans[-1] == char and
                ans[-2] == char
            ):
                if not heap:
                    break
                next_count, next_char = heapq.heappop(heap)
                next_count = -next_count
                ans.append(next_char)
                next_count -= 1
                if next_count > 0:
                    heapq.heappush(heap, (-next_count, next_char))
            else:
                ans.append(char)
                count -= 1
            if count > 0:
                heapq.heappush(heap, (-count, char))
        return "".join(ans)