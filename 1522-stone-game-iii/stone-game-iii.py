class Solution:
    def solve(self, idx, stoneValue, dp):
        if idx >= len(stoneValue):
            return 0
        if idx in dp:
            return dp[idx]
        max_score = float("-inf")
        cur_sum = 0
        for i in range(idx, min(idx + 3, len(stoneValue))):
            cur_sum += stoneValue[i]
            max_score = max(max_score, cur_sum - self.solve(i + 1, stoneValue, dp))
        dp[idx] = max_score
        return dp[idx]

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        score = self.solve(0, stoneValue, dict())
        if score < 0:
            return "Bob"
        elif score > 0:
            return "Alice"
        else:
            return "Tie"