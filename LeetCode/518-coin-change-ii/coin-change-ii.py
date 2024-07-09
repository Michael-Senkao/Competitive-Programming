class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(index, curr_sum):
            if curr_sum == amount:
                return 1
            if index >= n or curr_sum > amount:
                return 0
            
            return dp(index, curr_sum + coins[index]) + dp(index+1, curr_sum)

        n = len(coins)
        return dp(0, 0)