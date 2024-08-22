class Solution:
    def solve(self, start, end, cuts, dp):
        if start > end: return 0
        if (start, end) in dp:
            return dp[(start, end)]
        minimum_cuts = float("inf")
        for i in range(start, end + 1):
            cost = self.solve(start, i - 1, cuts, dp) + self.solve(i + 1, end, cuts, dp) + cuts[end + 1] - cuts[start - 1]
            minimum_cuts = min(minimum_cuts, cost)
        dp[(start, end)] = minimum_cuts
        return dp[(start, end)]

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        return self.solve(1, len(cuts) - 2, cuts, dict())