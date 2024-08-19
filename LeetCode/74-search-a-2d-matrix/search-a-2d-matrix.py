class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow(left, right):
            while left <= right:
                mid = left + (right - left)//2
                if matrix[mid][0] > target:
                    right = mid - 1
                elif matrix[mid][-1] < target:
                    left = mid + 1
                else:
                    return mid

            return -1
        

        def findCol(left, right):
            while left <= right:
                mid = left + (right - left)//2
                if matrix[row][mid] > target:
                    right = mid - 1
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    return mid
            
            return -1

        row = findRow(0, len(matrix) - 1)
        if row == -1:
            return False
        
        col = findCol(0, len(matrix[0]) - 1)

        return col != -1
        