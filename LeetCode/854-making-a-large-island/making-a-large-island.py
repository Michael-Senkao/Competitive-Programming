class Solution:
    def dfs(self,start_i,start_j, grid, island_id):
        stack = [(start_i, start_j)]
        grid[start_i][start_j] = island_id
        island_size = 1

        while stack:
            curr_i,curr_j = stack.pop()
            moves = [(curr_i+1,curr_j),(curr_i-1,curr_j),(curr_i,curr_j+1),(curr_i,curr_j-1)]

            for next_i,next_j in moves:
                if self.isValid(next_i, next_j, grid):
                    stack.append((next_i, next_j))
                    grid[next_i][next_j] = island_id
                    island_size += 1

        return island_size

    def isValid(self, row,col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid) and grid[row][col] == 1

    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        islands = [0,0,0]
        
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = self.dfs(i, j, grid, len(islands))
                    islands.append(size)

        if len(islands) == 3:
            return 1
        if len(islands) == 4:
            if islands[-1] == n*n:
                return islands[-1]
            return islands[-1] + 1   
        
        
        res = 0
        
            
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    surrounding_islands = set()
                    size = 0
                    moves = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                    for row,col in moves:
                        if 0 <= row < n and 0 <= col < n and grid[row][col] not in surrounding_islands:
                            size += islands[grid[row][col]]
                            surrounding_islands.add(grid[row][col])

                    res = max(res, size+1)
     
        return res