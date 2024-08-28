class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(index, hasStock):
            if index >= len(prices):
                return 0
            if (index, hasStock) in memo:
                return memo[(index, hasStock)]
            if hasStock:
                sell = prices[index] + dp(index + 1, False)
                not_sell = dp(index + 1, True)
                memo[(index, hasStock)] = max(sell, not_sell)
                return memo[(index, hasStock)]
            else:
                buy =  dp(index + 1, True) - prices[index]
                not_buy = dp(index + 1, False)
                memo[(index, hasStock)] = max(buy, not_buy)
                return memo[(index, hasStock)]

        return dp(0, False)