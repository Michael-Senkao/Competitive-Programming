class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def backtrack(index, curr_sum):
            if curr_sum == amount:
                return 1
            if index >= n or curr_sum > amount:
                return 0
            
            return backtrack(index, curr_sum + coins[index]) + backtrack(index+1, curr_sum)

        n = len(coins)
        return backtrack(0, 0)