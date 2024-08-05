class Solution:
    def solve(self, idx, bought, prices, fee, dp):
        if idx == len(prices):
            return 0
        if dp[idx][bought] != float('-inf'):
            return dp[idx][bought]
        if bought == 0:
            dp[idx][bought] = max(-prices[idx] + self.solve(idx + 1, 1, prices, fee, dp), self.solve(idx + 1, 0, prices, fee, dp))
        else:
            dp[idx][bought] = max(prices[idx] + self.solve(idx + 1, 0, prices, fee, dp) - fee, self.solve(idx + 1, 1, prices, fee, dp))
        return dp[idx][bought]


    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[float('-inf') for j in range(2)] for i in range(len(prices))]
        return self.solve(0, 0, prices, fee, dp)