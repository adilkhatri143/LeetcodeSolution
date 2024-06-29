class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        
        def dfs(inode, temp, visited):
            nonlocal graph
            visited[inode] = 1
            for nbr in graph[inode]:
                if not visited[nbr]:
                    temp.append(nbr)
                    dfs(nbr, temp, visited)

        answer = list() 
        for i in range(n):
            temp = list()
            visited = [0 for i in range(n)]
            dfs(i, temp, visited)
            temp.sort()
            answer.append(temp)
        return answer
