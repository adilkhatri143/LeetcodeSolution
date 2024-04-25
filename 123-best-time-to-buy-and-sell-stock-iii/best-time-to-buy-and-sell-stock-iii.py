class Solution:
    def solve(self, idx, buy, prices, k, dp):
        if idx == len(prices):
            return 0
        if k == 0:
            return 0

        if (idx, buy, k) in dp:
            return dp[(idx, buy, k)]

        if buy == 1:
            dp[(idx, buy, k)] = max(
                -prices[idx] + self.solve(idx + 1, buy - 1, prices, k, dp),
                self.solve(idx + 1, buy, prices, k, dp)
            )
            return dp[(idx, buy, k)]
        else:
            dp[(idx, buy, k)] = max(
                prices[idx] + self.solve(idx + 1, buy + 1, prices, k - 1, dp),
                self.solve(idx + 1, buy, prices, k, dp)
            )
            return dp[(idx, buy, k)]
        

    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        return self.solve(0, 1, prices, 2, dp)