class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Helper function to add valid neighboring cells to the queue
        def addNext(r, c, q, ROWS, COLS):
            # Define possible moves: up, down, left, and right
            moves = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            
            for i, j in moves:
                # Check if the move is within bounds, is a '.', and hasn't been visited
                if (0 <= i < ROWS 
                    and 0 <= j < COLS 
                    and maze[i][j] == '.' 
                    and (i, j) not in visited):
                    q.append((i, j))  # Add the valid move to the queue
                    visited.add((i, j))  # Mark the cell as visited

        ROWS, COLS = len(maze), len(maze[0])  # Dimensions of the maze
        q = deque()  # Queue for BFS traversal
        visited = set()  # Set to track visited cells
        start_r, start_c = entrance  # Starting coordinates
        steps = 1  # Step counter to track the distance to the nearest exit
        
        # Mark the entrance as visited
        visited.add((start_r, start_c))
        # Add the initial neighbors of the entrance to the queue
        addNext(start_r, start_c, q, ROWS, COLS)
        
        # BFS traversal
        while q:
            n = len(q)  # Number of elements at the current BFS level
            for _ in range(n):
                r, c = q.popleft()  # Get the next cell to process
                
                # Check if the current cell is an exit
                if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                    return steps
                
                # Add the neighbors of the current cell to the queue
                addNext(r, c, q, ROWS, COLS)
            
            steps += 1  # Increment the step count after processing all cells at the current level

        # If no exit is found, return -1
        return -1
