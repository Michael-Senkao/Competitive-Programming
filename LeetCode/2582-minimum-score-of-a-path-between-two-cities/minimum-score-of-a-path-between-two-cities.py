class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        return self.helper(graph, n)

    def helper(self, graph, n):
        min_score = float('inf')
        visited = set()
        q = deque([1])

        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            for nei,score in graph[curr]:
                if nei not in visited:
                    min_score = min(min_score, score)
                    q.append(nei)
        
        return min_score
        