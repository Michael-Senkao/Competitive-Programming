class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def bfs(start_i, start_j):
            islands = [(start_i, start_j)]
            q = deque([(start_i, start_j)])
            visited2.add((start_i, start_j))

            while q:
                r,c = q.popleft()
                if (c + 1 < cols 
                    and grid2[r][c+1] == 1 and (r, c + 1) not in visited2):
                    visited2.add((r, c + 1))
                    q.append((r, c + 1))
                    islands.append((r, c + 1))
                if (c - 1 >= 0
                    and grid2[r][c - 1] == 1 and (r, c - 1) not in visited2):
                    visited2.add((r, c - 1))
                    q.append((r, c - 1))
                    islands.append((r, c - 1))
                if (r + 1 < rows 
                    and grid2[r + 1][c] == 1 and (r + 1, c) not in visited2):
                    visited2.add((r + 1, c))
                    q.append((r + 1, c))
                    islands.append((r + 1, c))
                if (r - 1 >= 0 
                    and grid2[r - 1][c] == 1 and (r - 1, c) not in visited2):
                    visited2.add((r - 1, c))
                    q.append((r - 1, c))
                    islands.append((r - 1, c))

            return islands
            

        rows, cols = len(grid1), len(grid1[0])
        islands2 = []
        visited2 = set()
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r,c) not in visited2:
                    islands2.append(bfs(r, c))
       
        for island in islands2:
            for r,c in island:
                if grid1[r][c] == 0:
                    break
            else:
                res += 1

        return res