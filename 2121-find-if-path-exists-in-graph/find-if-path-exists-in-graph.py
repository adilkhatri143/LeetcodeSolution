from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        visited = set()
        visited.add(source)
        q.append(source)
        while q:
            size = len(q)
            while size:
                node = q.popleft()
                for nbr in graph[node]:
                    if nbr == destination:
                        return True
                    if nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)
                size -= 1
        return False