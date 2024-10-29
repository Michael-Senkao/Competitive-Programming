class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        sset = set()
        result = -1
        for r in range(m):
            sset.add((r,0))
        
        while sset:
            next_set = set()
            for r,c in sset:
                # Top diagonal
                if r - 1 >= 0 and c + 1 < n and grid[r - 1][c + 1] > grid[r][c]:
                    next_set.add((r - 1, c + 1))
                # Bottom diagonal
                if r + 1 < m and c + 1 < n and grid[r + 1][c + 1] > grid[r][c]:
                    next_set.add((r + 1, c + 1))
                # Adjacent
                if c + 1 < n and grid[r][c + 1] > grid[r][c]:
                    next_set.add((r, c + 1))
            
            sset = next_set
            result += 1

        return result
        