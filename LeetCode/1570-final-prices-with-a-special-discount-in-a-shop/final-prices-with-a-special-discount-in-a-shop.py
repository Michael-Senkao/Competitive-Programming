class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        result = prices.copy()

        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                result[stack.pop()] -= prices[i]
            stack.append(i)

        return result