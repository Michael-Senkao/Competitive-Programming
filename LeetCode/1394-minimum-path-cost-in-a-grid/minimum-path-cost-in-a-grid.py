class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        
        for i in range(n):
            for j in range(m):
                dp[i][j] += grid[i][j]
                for k in range(m):
                    if i + 1 < n:
                        if dp[i+1][k] == 0:
                            dp[i+1][k] = dp[i][j] + moveCost[grid[i][j]][k]
                        else:
                            dp[i+1][k] = min(dp[i+1][k], dp[i][j] + moveCost[grid[i][j]][k])
        
        
        return min(dp[-1])