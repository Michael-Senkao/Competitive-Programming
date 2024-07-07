class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i - 1 >=0 and j >= 0:
                    dp[i-1][j] += dp[i][j]
                if i >= 0 and j - 1 >= 0:
                    dp[i][j-1] += dp[i][j]
        # print(dp)
        return dp[0][0]