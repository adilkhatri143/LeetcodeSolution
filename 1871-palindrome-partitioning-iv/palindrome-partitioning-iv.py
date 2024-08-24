class Solution:
    def solve(self, idx, s, dp, three_cuts):
        if idx == len(s):
            return three_cuts == 3
        if three_cuts >= 3:
            return False
        if (idx, three_cuts) in dp:
            return dp[(idx, three_cuts)]
        possible = False
        for i in range(idx, len(s)):
            if s[idx: i + 1] == s[idx: i + 1][::-1]:
                possible |= self.solve(i + 1, s, dp, three_cuts + 1)
        dp[(idx, three_cuts)] = possible
        return dp[(idx, three_cuts)]
    
    def checkPartitioning(self, s: str) -> bool:
        return self.solve(0, s, dict(), 0)
        