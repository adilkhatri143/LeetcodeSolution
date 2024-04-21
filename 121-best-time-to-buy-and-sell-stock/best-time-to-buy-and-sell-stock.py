class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        max_profit = float('-inf')
        for price in prices:
            buy = min(buy, price)
            max_profit = max(max_profit, price - buy)
        return max_profit
