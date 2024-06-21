class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i):
            
            if i == len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i] or (r,c) in visited:
                return False
            visited.add((r,c))
            res = any([dfs(r+1,c,i+1), dfs(r-1,c,i+1), dfs(r,c+1,i+1), dfs(r,c-1,i+1)])
            visited.remove((r,c))
            return res
        for i in range(rows):
            for j in range(cols):
                
                if dfs(i,j,0):
                    return True
                visited.clear()
                
        return False

