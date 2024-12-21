class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n==1:
            return 1

        degree = [0]*n # To track the degree of each node
        graph = defaultdict(list) # Adjacency list for tree

        # Create adjacency list for the tree
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        q = deque()
        count = 0

        # Initialize the queue with the leaf nodes
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        # Use BFS to traverse the tree
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
