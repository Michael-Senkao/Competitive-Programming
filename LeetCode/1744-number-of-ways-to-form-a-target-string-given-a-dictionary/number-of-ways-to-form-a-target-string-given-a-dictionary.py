class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @cache
        def dfs(i,j):
            if i == len(words[0]) or j == len(target):
                return 1 if j == len(target) else 0

            take = 0
            count = vals[i][ord(target[j])-97]

            if count:
                take =  (count * dfs(i+1,j + 1)) % mod
            not_take = dfs(i+1,j) % mod
            return (take + not_take) % mod


        n = len(words[0])
        if n < len(target):
            return 0
        
        
        vals = [[0] * 26 for _ in range(n)]
        
        for i in range(n):
            for word in words:
                vals[i][ord(word[i])-97]+=1
        
        mod = 10**9 + 7
    
        return dfs(0,0) 

                
            