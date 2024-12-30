class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        def backtrack(length):
            if length > high:
                return 0
            
            if length in memo:
                return memo[length]

            add_zero = backtrack(length + zero) % MOD
            add_one = backtrack(length + one) % MOD

            memo[length] = (add_zero + add_one + (low <= length <= high)) % MOD


            return memo[length]

        MOD = 10**9 + 7
        # dp = [-1]*(high + 1)

        memo = {}

        ans = backtrack(0)
        # print(dp)
        return ans
            
        