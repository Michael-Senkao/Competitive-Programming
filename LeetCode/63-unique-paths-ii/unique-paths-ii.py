class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    continue
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j-1]
        # print(dp)
        return dp[rows-1][cols-1]

        # Top down DP
        # def dp(i,j):
        #     if i >= rows or j >= cols or obstacleGrid[i][j] == 1:
        #         return 0

        #     if memo[i][j]:
        #         return memo[i][j]
            
        #     if i==rows-1 and j==cols-1:
        #         return 1

        #     right = dp(i, j+1)
        #     down = dp(i+1, j)
        #     memo[i][j] = (right + down)
        #     return memo[i][j]

        # memo = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # memo[0][0] = dp(0,0)
        
        # return memo[0][0]
            