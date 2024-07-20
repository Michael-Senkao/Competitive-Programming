class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def bfs(i,j):
            def valid(r,c):
                return r>=0 and c>=0 and r < rows and c<cols and maze[r][c] != "+" and (r,c) not in visited
            q = deque()
            visited = set()
            q.append((i,j,0))
            visited.add((i,j))
            while q:
                row,col,cost = q.popleft()
                
                if (row == 0 or col == 0 or row == rows-1 or col == cols-1):
                    if (row,col) != (i,j):
                        return cost
                if valid(row, col+1):
                    q.append((row,col+1, cost + 1))
                    visited.add((row,col + 1))

                if valid(row, col-1):
                    q.append((row,col-1, cost + 1))
                    visited.add((row,col - 1))
                if valid(row+1, col):
                    q.append((row + 1,col, cost + 1))
                    visited.add((row + 1,col))
                if valid(row-1, col):
                    q.append((row-1,col, cost + 1))
                    visited.add((row - 1,col))

            return -1
        rows,cols = len(maze),len(maze[0])
        return bfs(entrance[0], entrance[1])
            