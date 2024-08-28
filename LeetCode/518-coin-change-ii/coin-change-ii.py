class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(index, total):
            if index == len(coins):
                return 1 if total==amount else 0
            if total == amount:
                return 1
            if total > amount:
                return 0
            return dp(index, total + coins[index]) + dp(index + 1, total)

        return dp(0, 0)
            