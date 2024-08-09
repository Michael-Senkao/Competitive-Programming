class UnionFind:
    def __init__(self, rows, cols, grid):
        self.parent = {}
        self.size = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                self.parent[(i,j)] = (i, j)
                self.size[i][j] = grid[i][j]
    
    def find(self, x: tuple):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x:tuple, y:tuple):
        r1,c1 = self.find(x)
        r2,c2 = self.find(y)
        
        if (r1,c1) != (r2,c2):
            if self.size[r1][c1] > self.size[r2][c2]:
                self.parent[(r2,c2)] = (r1,c1)
                self.size[r1][c1] += self.size[r2][c2]
            else:
                self.parent[(r1,c1)] = (r2,c2)
                self.size[r2][c2] += self.size[r1][c1]


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def connect(i,j):
            if valid(i, j + 1):
                dsu.union((i,j), (i, j + 1))
            if valid(i, j - 1):
                dsu.union((i,j), (i, j - 1))
            if valid(i + 1, j):
                dsu.union((i,j), (i + 1, j))
            if valid(i - 1, j):
                dsu.union((i,j), (i - 1, j))

        def valid(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return False
            return True

        rows,cols = len(grid), len(grid[0])
        dsu = UnionFind(rows, cols, grid)

        for i in range(rows):
            for j in range(cols):
                if valid(i,j):
                    connect(i,j)
        
        return max([max(row) for row in dsu.size])