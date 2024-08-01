class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = {i for i in range(1, len(isConnected) + 1)}
        graph = {i: list() for i in range(1, len(isConnected) + 1)}
        visited = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    graph[i + 1].append(j + 1)
        
        answer = 0
        def dfs(graph, node, cities, visited):
            visited.add(node)
            cities.remove(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(graph, nbr, cities, visited)

        for i in range(1, len(isConnected) + 1):
            if i not in visited:
                dfs(graph, i, cities, visited)
                answer += 1
        return answer