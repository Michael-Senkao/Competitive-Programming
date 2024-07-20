class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows,cols = len(rowSum), len(colSum)
        result = [[0 for _ in range(cols)] for _ in range(rows)]


        for row in range(rows):
            for col in range(cols):
                if rowSum[row] > 0 and colSum[col]:
                    minimum = min(rowSum[row], colSum[col])
                    result[row][col] = minimum
                    rowSum[row] -= minimum
                    colSum[col] -= minimum
        return result