class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n==1:
            return 1

        degree = [0]*n
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        q = deque()
        count = 0
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        while q:
            # print(q)
            node = q.popleft()
            # print(node, values[node], values[node]%k==0)
            if values[node] % k == 0:
                count += 1
                values[node] = 0
            for nei in graph[node]:
                values[nei] += values[node]
                if degree[nei] == 1:
                    continue
                degree[nei] -= 1
                if degree[nei] == 1:
                    q.append(nei)
                
        
        return count
