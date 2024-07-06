class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if (i,j) in visited or i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j]==0:
                return 0
            visited.add((i, j))

            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    res = max(res, dfs(r,c))

        return res