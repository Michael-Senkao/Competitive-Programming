class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid2[i][j]==0 or (i,j) in visited:
                return True
            
            visited.add((i,j))
            result = True

            if grid1[i][j] == 0:
                result = False
            
            result = dfs(i,j+1) and result
            result = dfs(i, j-1) and result 
            result = dfs(i+1, j) and result
            result = dfs(i-1, j) and result
            return result
            
            
            

        rows,cols = len(grid1), len(grid1[0])
        visited = set()
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j]==1 and (i,j) not in visited and dfs(i,j):
                    res += 1
        return res