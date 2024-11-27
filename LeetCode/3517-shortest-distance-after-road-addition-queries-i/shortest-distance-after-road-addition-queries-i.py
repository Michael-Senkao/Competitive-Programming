class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def update(node):
            for next_node in graph[node]:
                if distance[node] + 1 < distance[next_node]:
                    distance[next_node] = distance[node] + 1
                    update(next_node)


        graph = defaultdict(list)
        distance = [0]
        res = []
        for i in range(1,n):
            distance.append(i)
            graph[i-1].append(i)
        
        for u,v in queries:
            graph[u].append(v)
            update(u)
            res.append(distance[-1])

        return res