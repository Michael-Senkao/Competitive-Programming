class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def bfs(a,b):
            q = deque([(a, 1)])
            visited = set([a])

            while q:
                curr,val = q.popleft()
                if curr == b:
                    return val
                for nei, cost in graph[curr]:
                    if nei not in visited:
                        q.append((nei, val*cost))
                        visited.add(nei)
            return -1

        graph = defaultdict(list)
        res = []

        for i, (a,b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))

       
        for a,b in queries:
            if a not in graph or b not in graph:
                res.append(-1)
                continue
            
            res.append(bfs(a,b))
       
        return res
        