class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            for nbr in rooms[i]:
                graph[i].append(nbr)
        visited = set()
        def dfs(graph, node):
            nonlocal visited
            nonlocal rooms
            visited.add(node)
            if len(visited) == len(rooms):
                return True
            answer = False
            for nbr in graph[node]:
                if nbr not in visited:
                    answer = answer or dfs(graph, nbr)
            return answer
        return dfs(graph, 0)