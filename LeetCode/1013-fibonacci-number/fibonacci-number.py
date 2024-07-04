class Solution:
    memo = [0, 1]
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        if len(self.memo) <= n:
            self.memo.append(self.fib(n-1) + self.fib(n-2))
        return self.memo[n]
        
