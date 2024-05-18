class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        prefix_sum = [[0]*cols for i in range(rows)]
        ans = 0

        # Compute the sub-matrix sum (i.e. prefix sum) 
        for row in range(1,rows):
            for col in range(1, cols):
                prefix_sum[row][col] = matrix[row-1][col-1] + prefix_sum[row-1][col] + prefix_sum[row][col -1] - prefix_sum[row-1][col-1]

        # Iterate over all possible sub-matrices and comparing their sums with target and updating the answer when the sum equals the target 
        for r1 in range(1, rows):
            for r2 in range(r1, rows):
                count = defaultdict(int) # Store the prefix sum seen so far
                count[0] = 1
                for c in range(1, cols):
                    current_sum = prefix_sum[r2][c] - prefix_sum[r1-1][c]
                    diff = current_sum - target
                    ans += count[diff]
                    count[current_sum] += 1    
        
        return ans
