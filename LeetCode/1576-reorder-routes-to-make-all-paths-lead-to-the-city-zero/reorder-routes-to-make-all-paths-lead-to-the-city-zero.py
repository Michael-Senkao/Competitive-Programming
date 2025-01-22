class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False]*n

        for start,end in connections:
            graph[start].append((end, False))
            graph[end].append((start, True))

        q = deque([0])
        visited[0] = True
        reorders = 0
        
        while q:
            curr = q.popleft()
            for nei,canReach in graph[curr]:
                if visited[nei]:
                    continue

                if not canReach:
                    reorders += 1

                q.append(nei)
                visited[nei] = True

        return reorders