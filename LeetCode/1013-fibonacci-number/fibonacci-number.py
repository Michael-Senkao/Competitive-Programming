class Solution:
    
    def fib(self, n: int) -> int:
        def dp(n):
            if n < 2:
                return n
            
            if len(memo) <= n:
                memo.append(dp(n-1) + dp(n-2))
            return memo[n]
        
        memo = [0, 1]
        return dp(n)
        
