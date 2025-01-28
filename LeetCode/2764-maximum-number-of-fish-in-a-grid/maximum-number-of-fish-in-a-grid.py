from typing import List

class Solution:
    def collectFish(self, row: int, col: int, grid: List[List[int]]) -> int:
        """
        Performs DFS to collect fish from a connected component in the grid.
        
        Args:
            row (int): Current row index.
            col (int): Current column index.
            grid (List[List[int]]): A 2D grid representing fish quantities in cells.
        
        Returns:
            int: Total fish collected from the connected component.
        """
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0  # Out of bounds or already visited
        
        fish = grid[row][col]
        grid[row][col] = 0  # Mark the cell as visited
        
        # Explore in all four directions
        return (fish +
                self.collectFish(row, col + 1, grid) +  # Right
                self.collectFish(row, col - 1, grid) +  # Left
                self.collectFish(row - 1, col, grid) +  # Up
                self.collectFish(row + 1, col, grid))   # Down

    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum fish count that can be collected from any connected component.
        
        Args:
            grid (List[List[int]]): A 2D grid of integers where each cell contains fish quantities.
        
        Returns:
            int: Maximum fish count from any connected component in the grid.
        """
        if not grid or not grid[0]:
            return 0  # Edge case: empty grid

        rows, cols = len(grid), len(grid[0])
        max_fish = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:  # Start DFS from cells with fish
                    max_fish = max(max_fish, self.collectFish(row, col, grid))

        return max_fish
