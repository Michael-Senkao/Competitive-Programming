class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(index, holding):
            if index >= len(prices):
                return 0
            
            if (index, holding) in memo:
                return memo[(index, holding)]
            
            max_profit = dp(index + 1, holding)  # Skip current day

            if holding:
                # If holding a stock, you can sell
                max_profit = max(max_profit, dp(index + 2, False) + prices[index])
            else:
                # If not holding, you can buy
                max_profit = max(max_profit, dp(index + 1, True) - prices[index])

            memo[(index, holding)] = max_profit
            return max_profit

        return dp(0, False)
