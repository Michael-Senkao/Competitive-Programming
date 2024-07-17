class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            visited.add(node)
            res = 0
            for nei in adj[node]:
                if nei not in visited:
                    res += dfs(nei)
            
            if hasApple[node] or res > 0:
                res += 1
    
            return res

        
        adj = defaultdict(list)
        visited = set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        result = dfs(0) - 1
        return result*2 if result > 0 else 0