class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        n = len(graph)

        def dfs(node, path):
            if node == n-1:
                res.append(path)
                return
            for neighbor in graph[node]:
                dfs(neighbor, path + [neighbor])
        
        dfs(0, [0])
        return res
            