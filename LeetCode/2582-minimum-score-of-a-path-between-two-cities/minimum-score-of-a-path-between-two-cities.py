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
        visited.add(1)

        while q:
            curr = q.popleft()

            for nei,score in graph[curr]:
                min_score = min(min_score, score)
                if nei not in visited:
                    q.append(nei)
                    visited.add(curr)
        
        return min_score
        