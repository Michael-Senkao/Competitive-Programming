class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def addNext(r,c, q, ROWS, COLS):
            moves = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]

            for i,j in moves:
                if (0 <= i < ROWS 
                    and 0 <= j < COLS 
                    and maze[i][j] == '.' 
                    and (i,j) not in visited):
                    q.append((i,j))
                    visited.add((i,j))
        
        ROWS,COLS = len(maze), len(maze[0])
        q = deque()
        visited = set()
        start_r,start_c = entrance
        steps = 1
      
        visited.add((start_r, start_c))
        addNext(start_r, start_c, q, ROWS,COLS)
        
        while q:
            n = len(q)
            for i in range(len(q)):
                r,c = q.popleft()
                if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                    return steps
                addNext(r,c,q,ROWS,COLS)

            steps += 1

        return -1