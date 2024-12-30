class Solution:
    def climbStairs(self, n: int) -> int:
        def backtrack(length):
            if length < n:
                if dp[length] != -1:
                    return dp[length]
                dp[length] = backtrack(length + 1) + backtrack(length + 2)

                return dp[length]
            return length == n


        dp = [-1]*(n + 1)

        return backtrack(0)
