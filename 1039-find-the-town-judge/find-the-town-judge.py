class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_degree = [0 for i in range(n + 1)]
        outgoing_degree = [0 for i in range(n + 1)]
        for i in range(len(trust)):
            outgoing_degree[trust[i][0]] += 1
            incoming_degree[trust[i][1]] += 1
        for i in range(1, n + 1):
            if outgoing_degree[i] == 0 and incoming_degree[i] == n - 1:
                return i
        return -1