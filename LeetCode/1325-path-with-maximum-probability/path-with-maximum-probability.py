class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        max_prob = [0]*n
        max_prob[start_node] = 1
        res = 0
        for i in range(len(edges)):
            u,v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        q = deque([start_node])
        visited = set([start_node])

        while q:
            curr = q.popleft()
            for nei, prob in graph[curr]:
                if max_prob[curr]*prob > max_prob[nei]:
                    max_prob[nei] = max_prob[curr]*prob
                    q.append(nei)
        
        return max_prob[end_node]


        