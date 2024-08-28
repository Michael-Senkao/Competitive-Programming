class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(index, hasStock):
            if index >= len(prices):
                return 0

            if hasStock:
                sell = prices[index] + dp(index + 1, False)
                not_sell = dp(index + 1, True)
                return max(sell, not_sell)
            else:
                buy =  dp(index + 1, True) - prices[index]
                not_buy = dp(index + 1, False)
                return max(buy, not_buy)

        return dp(0, False)