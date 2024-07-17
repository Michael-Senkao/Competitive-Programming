class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        result = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j, 0))
        
        while q:
            i,j,distance = q.popleft()
            if i < 0 or j < 0 or i >= rows or j >= cols or (i,j) in visited:
                continue
            visited.add((i,j))
            result[i][j] = distance
            q.append((i, j+1, distance + 1))
            q.append((i, j -1, distance + 1))
            q.append((i+1, j, distance + 1))
            q.append((i-1, j, distance + 1))


        return result