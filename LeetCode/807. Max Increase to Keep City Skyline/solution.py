class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        max_row = [0]*rows
        max_col = [0]*cols
        res = 0

        # Find the maximum element in each row and each column
        for i in range(rows):
            for j in range(cols):
                max_row[i] = max(max_row[i], grid[i][j])
                max_col[j] = max(max_col[j], grid[i][j])

        # Take the minimum of the maximum element in row r and column c and add the difference it and grid[r][c] to the result
        for i in range(rows):
            for j in range(cols):
                res += min(max_row[i], max_col[j]) - grid[i][j]
       
        return res
