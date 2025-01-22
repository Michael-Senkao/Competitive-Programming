class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(isWater), len(isWater[0])
        q = deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]:
                    q.append((i,j,0))
                    visited.add((i,j))

        while q:
            row,col,height = q.popleft()
            isWater[row][col] = height
            nei = [[row, col - 1], [row, col + 1], [row-1, col], [row+1, col]]

            for r,c in nei:
                if 0 <= r < rows and 0 <= c < cols and (r,c) not in visited:
                    q.append((r,c, height + 1))
                    visited.add((r,c))

        return isWater