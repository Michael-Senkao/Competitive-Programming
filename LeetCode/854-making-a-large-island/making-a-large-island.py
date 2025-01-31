from typing import List
from collections import deque

class Solution:
    def bfs(self, start_i: int, start_j: int, grid: List[List[int]], island_id: int) -> int:
        """ Perform BFS to mark the island and return its size. """
        queue = deque([(start_i, start_j)])
        grid[start_i][start_j] = island_id
        island_size = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        while queue:
            curr_i, curr_j = queue.popleft()
            for di, dj in directions:
                next_i, next_j = curr_i + di, curr_j + dj
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid) and grid[next_i][next_j] == 1:
                    queue.append((next_i, next_j))
                    grid[next_i][next_j] = island_id
                    island_size += 1

        return island_size

    def largestIsland(self, grid: List[List[int]]) -> int:
        """ Returns the largest possible island size after flipping one '0' to '1'. """
        n = len(grid)
        island_id = 2  # Start from 2 to differentiate from land (1)
        island_sizes = {0: 0}  # Store island sizes, mapping ID to size

        # Step 1: Find all islands and mark them
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = self.bfs(i, j, grid, island_id)
                    island_id += 1

        max_island = max(island_sizes.values()) if island_sizes else 0  # Handle no land case

        # Step 2: Try flipping each '0' to connect islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    new_size = 1  # Start with 1 (flipping this cell to '1')
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        row, col = i + di, j + dj
                        if 0 <= row < n and 0 <= col < n and grid[row][col] > 1:
                            seen_islands.add(grid[row][col])
                    new_size += sum(island_sizes[is_id] for is_id in seen_islands)
                    max_island = max(max_island, new_size)

        return max_island
