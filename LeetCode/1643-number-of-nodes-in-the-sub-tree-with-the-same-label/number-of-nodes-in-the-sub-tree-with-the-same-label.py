class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node):
            if node in visited:
                return defaultdict(int)
            
            visited.add(node)
            curr_label = labels[node]
            counts = defaultdict(int)

            for neighbor in adj[node]:
                result = dfs(neighbor)
                for label,count in result.items():
                    counts[label] += count
            
            counts[curr_label] += 1
            ans[node] = counts[curr_label]
            return counts

            


        adj = defaultdict(list)
        visited = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = [0 for _ in range(n)]
        dfs(0)
        return ans 

            
