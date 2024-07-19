class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix),len(matrix[0])
        minRows = [min(matrix[i]) for i in range(rows)]
        maxCols = []
        res = []

        for c in range(cols):
            maximum = 0
            for r in range(rows):
                maximum = max(maximum, matrix[r][c])

            maxCols.append(maximum)

        for i in range(rows):
            for j in range(cols):
                num = matrix[i][j]
                if num == minRows[i] and num == maxCols[j]:
                    res.append(num)

        return res