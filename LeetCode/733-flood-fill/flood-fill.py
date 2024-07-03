class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and image[r][c] == prevColor and image[r][c] != color:
                visited.add((r,c))
                image[r][c] = color
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
                
        
        m = len(image)
        n = len(image[0])
        prevColor = image[sr][sc]
        visited = set()
        

        dfs(sr, sc)

        return image
        