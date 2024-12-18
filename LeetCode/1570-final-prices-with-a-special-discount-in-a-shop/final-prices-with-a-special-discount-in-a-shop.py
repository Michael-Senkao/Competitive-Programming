class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        ans = prices.copy()

        for i in range(n-1, -1,- 1):
            print(stack)
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack and prices[i] >= stack[-1]:
                ans[i] -= stack[-1]
            stack.append(prices[i])


        return ans