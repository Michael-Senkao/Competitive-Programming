class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def bfs(i):
            if color[i-1]:
                return True
            q = deque([i])
            color[i-1] = -1
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if color[nei-1] and color[nei-1]==color[curr-1]:
                        return False
                    elif not color[nei-1]:
                        q.append(nei)
                        color[nei-1] = -1 * color[curr-1]

            return True


        graph = defaultdict(list)
        color = [0 for _ in range(n)]
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        for key in graph:
            if not bfs(key):
                return False
        return True