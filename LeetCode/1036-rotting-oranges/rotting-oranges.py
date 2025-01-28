"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows,cols = len(grid), len(grid[0])
        q = deque()
        
        # Initialize queue with initial rotten fruits
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))

        minute = 0
        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                moves = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for r,c in moves:
                    if r < 0 or r == rows or c < 0 or c == cols:
                        continue
                    if grid[r][c] == 1:
                        q.append((r,c))
                        grid[r][c] = 2

            minute += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1 # Can't make this one rotten

        return minute - 1 if minute > 0 else 0
