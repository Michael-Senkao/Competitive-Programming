class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Finds the shortest path to the nearest exit from the given entrance.
        
        Args:
            maze (List[List[str]]): 2D grid representing the maze.
            entrance (List[int]): Starting coordinates [row, col].
        
        Returns:
            int: The minimum number of steps to the nearest exit, or -1 if none exists.
        """
        from collections import deque

        def enqueue_valid_neighbors(row, col, queue, rows, cols):
            """Adds all valid neighboring cells to the BFS queue."""
            moves = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for r, c in moves:
                if (0 <= r < rows and 0 <= c < cols and maze[r][c] == '.'):
                    queue.append((r, c))
                    # visited.add((r, c))
                    # Assuming we are allowed to alter the input maze
                    maze[r][c] = '+'

        rows, cols = len(maze), len(maze[0])
        queue = deque()
        # visited = set()
        start_row, start_col = entrance


        # Initialize BFS
        # visited.add((start_row, start_col))
        maze[start_row][start_col] = '+'
        enqueue_valid_neighbors(start_row, start_col, queue, rows, cols)
        steps = 1

        # BFS loop
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row in [0, rows - 1] or col in [0, cols - 1]:
                    return steps
                enqueue_valid_neighbors(row, col, queue, rows, cols)
            steps += 1

        return -1
