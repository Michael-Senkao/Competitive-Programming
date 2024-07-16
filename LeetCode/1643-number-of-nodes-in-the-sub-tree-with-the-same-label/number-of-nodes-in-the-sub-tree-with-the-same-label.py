class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node):
            if node in visited:
                return ""
            
            visited.add(node)
            label = labels[node]
            sub = label[::]
            for neighbor in adj[node]:
                sub += dfs(neighbor)
            
            ans[node] = sub.count(label)
            return sub

            


        adj = defaultdict(list)
        visited = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = [0 for _ in range(n)]
        dfs(0)
        return ans 

            
