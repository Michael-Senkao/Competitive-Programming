class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def recur_joseph(n, k): 
            if (n == 1): 
                return 1
            else: 
                return (recur_joseph(n-1,k)+ k-1)% n + 1

        return recur_joseph(n, k)