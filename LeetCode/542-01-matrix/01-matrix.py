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
                    visited.add((i,j))
        
        while q:
            i,j,distance = q.popleft()
            if i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            result[i][j] = distance
            if (i, j+1) not in visited:
                q.append((i, j+1, distance + 1))
                visited.add((i,j+1))
            if (i, j-1) not in visited:
                q.append((i, j -1, distance + 1))
                visited.add((i,j-1))
            if (i+1, j) not in visited:
                q.append((i+1, j, distance + 1))
                visited.add((i+1,j))
            if (i-1, j) not in visited:
                q.append((i-1, j, distance + 1))
                visited.add((i-1,j))


        return result