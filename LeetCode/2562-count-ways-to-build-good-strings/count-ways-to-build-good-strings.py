class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        def backtrack(length):
            if length > high:
                return 0
            
            if dp[length] != -1:
                return dp[length]

            add_zero = backtrack(length + zero) % MOD
            add_one = backtrack(length + one) % MOD

            dp[length] = (add_zero + add_one + (low <= length <= high)) % MOD


            return dp[length]

        MOD = 10**9 + 7
        dp = [-1]*(high + 1)

        ans = backtrack(0)
        
        return ans
            
        