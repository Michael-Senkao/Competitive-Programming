class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        # adjList = defaultdict(list)
        # for i in range(len(graph)):
        res = []
        n = len(graph)

        def dfs(node, path):
            if node == n-1:
                res.append(path)
                return
            for node in graph[node]:
                dfs(node, path + [node])
        
        dfs(0, [0])
        return res
            