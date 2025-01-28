class Solution:
    def dfs(self, row,col, grid):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or not grid[row][col]:
            return 0

        fish = grid[row][col]
        grid[row][col] = 0
        return (fish +
                self.dfs(row, col + 1, grid) +
                self.dfs(row, col - 1, grid) +
                self.dfs(row - 1, col, grid) +
                self.dfs(row + 1, col, grid)
        )

    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        result = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    result = max(result, self.dfs(row, col, grid))

        return result