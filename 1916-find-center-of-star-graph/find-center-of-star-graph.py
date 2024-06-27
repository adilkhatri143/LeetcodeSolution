class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        len_answer = answer = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            if len_answer < len(graph[u]):
                len_answer = len(graph[u])
                answer = u
            if len_answer < len(graph[v]):
                len_answer = len(graph[v])
                answer = v
        return answer