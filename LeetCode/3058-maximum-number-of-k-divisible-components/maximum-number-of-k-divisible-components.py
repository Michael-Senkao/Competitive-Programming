class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n == 1:
            return 1
        graph = defaultdict(list)
        degree = [0]*n

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        q = deque()
        count = 0
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
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