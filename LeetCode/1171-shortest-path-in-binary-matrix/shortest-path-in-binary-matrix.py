class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(start_i,start_j):
            
            q = deque([(start_i, start_j, 1)])

            while q:
                i,j,cost = q.popleft()
                if (i,j) == (n-1, n-1):
                    
                    return cost
                if isValid(i,j):
                    visited.add((i,j))
                    q.append((i, j + 1, cost + 1))
                    q.append((i, j - 1, cost + 1))
                    q.append((i+1, j, cost + 1))
                    q.append((i-1, j, cost + 1))
                    q.append((i+1, j + 1, cost + 1))
                    q.append((i+1, j - 1, cost + 1))
                    q.append((i - 1, j + 1, cost + 1))
                    q.append((i - 1, j - 1, cost + 1))
            return -1
        
        def isValid(i,j):
            if i < 0 or j < 0 or i >= n or j >= n or (i,j) in visited or grid[i][j]==1:
                return False
            return True

        visited = set()
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]==1:
            return -1
        return bfs(0,0)
