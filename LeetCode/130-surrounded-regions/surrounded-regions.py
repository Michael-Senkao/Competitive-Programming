class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            if (i < 0 or j < 0 or i >= rows or j >= cols):
                return False
            
            if board[i][j] == 'X' or (i,j) in region:
                return True
            visited.add((i, j))
            region.add((i,j))
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            return all([left,right,up,down])

        
        rows,cols = len(board), len(board[0])
        visited = set()
        region = set()

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and (i,j) not in visited:
                    region.clear()
                    if dfs(i,j):
                        for r,c in region:
                            board[r][c] = 'X'
                


            
        