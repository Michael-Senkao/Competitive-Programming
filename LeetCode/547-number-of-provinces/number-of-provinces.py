class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(start):
            visited.add(start)
            q = deque([start])
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        graph = defaultdict(list)
        provinces = 0
        visited = set()

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] and i != j:
                    graph[i].append(j)
                    graph[j].append(i)

        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                bfs(i)

        return provinces