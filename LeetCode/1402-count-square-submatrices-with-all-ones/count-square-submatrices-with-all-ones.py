class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i-1>=0:
                    matrix[i][j]+=matrix[i-1][j]
                if j-1>=0:
                    matrix[i][j]+=matrix[i][j-1]
                if i-1>=0 and j-1>=0:
                    matrix[i][j]-=matrix[i-1][j-1]
        result = 0
        for i in range(1,min(m,n) + 1):
            start_row,end_row=0,i-1
            while end_row<m:
                start_column,end_column=0,i-1
                while end_column<n:
                    val = matrix[end_row][end_column]
                    if start_column-1>=0:
                        val-=matrix[end_row][start_column-1]
                    if start_row-1>=0:
                        val-=matrix[start_row-1][end_column]
                    if start_column-1 >=0 and start_row-1>=0:
                        val+=matrix[start_row-1][start_column-1]
                    if val == i*i:
                        result+=1
                    end_column+=1
                    start_column+=1
                end_row+=1
                start_row+=1
        return result