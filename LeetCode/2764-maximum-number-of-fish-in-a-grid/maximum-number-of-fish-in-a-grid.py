class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(start_r, start_c):
            q = deque()
            fishes = 0
            q.append((start_r, start_c))
            visited.add((start_r, start_c))

            while q:
                r,c = q.popleft()
                fishes += grid[r][c]
                if valid(r, c + 1):
                    q.append((r, c + 1))
                    visited.add((r, c + 1))
                if valid(r, c - 1):
                    q.append((r, c - 1))
                    visited.add((r, c - 1))
                if valid(r + 1, c ):
                    q.append((r + 1, c))
                    visited.add((r + 1, c))
                if valid(r - 1, c):
                    q.append((r - 1, c))
                    visited.add((r - 1, c))
            return fishes
        
        def valid(i,j):
            if i < 0 or j < 0 or i == rows or j == cols or (i,j) in visited or grid[i][j] == 0:
                return False
            return True
        

        rows, cols = len(grid), len(grid[0])
        visited = set()
        result = 0

        for r in range(rows):
            for c in range(cols):
                if valid(r, c):
                    # print(result, end = " ")
                    result = max(result, bfs(r, c))
                    print(r,c, result)
        
        return result
                
