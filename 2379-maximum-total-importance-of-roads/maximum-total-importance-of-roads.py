import heapq
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [[0, i] for i in range(n)]
        for u, v in roads:
            indegree[u][0] += 1
            indegree[v][0] += 1
        heapq.heapify(indegree)
        ranking = [0] * n
        i = 1
        while indegree:
            rank, idx = heapq.heappop(indegree)
            ranking[idx] = i
            i += 1
        total = 0
        for u, v in roads:
            total += ranking[u] + ranking[v]
        return total

