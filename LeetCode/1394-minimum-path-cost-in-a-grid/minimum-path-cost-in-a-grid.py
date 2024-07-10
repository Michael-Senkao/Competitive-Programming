class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        
        print(dp)
        for i in range(n-1):
            for j in range(m):
                dp[i][j] += grid[i][j]
                for k in range(m):
                    if dp[i+1][k] == 0:
                        dp[i+1][k] = dp[i][j] + moveCost[grid[i][j]][k]
                    else:
                        dp[i+1][k] = min(dp[i+1][k], dp[i][j] + moveCost[grid[i][j]][k])
        
        res = float("inf")
        for i in range(m):
            res = min(res, dp[n-1][i] + grid[n-1][i])
        return res