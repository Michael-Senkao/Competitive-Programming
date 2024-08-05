class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def ans():
            while len(max_heap) > k:
                heappop(max_heap)
            return -max_heap[0]
        rows = cols = len(matrix)
        max_heap = []
        heapify(max_heap)


        for r in range(rows):
            if len(max_heap) >= k and r > 0 and matrix[r][0] >= matrix[r-1][cols - 1]:
                return ans()
            for c in range(cols):
                heappush(max_heap, -matrix[r][c])
        
        return ans()