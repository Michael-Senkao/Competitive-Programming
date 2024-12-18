class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        

        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices