class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adjList = defaultdict(set)
        
        res = 0

        for u,v in roads:
            adjList[u].add(v)
            adjList[v].add(u)

        for i in range(n):
            for j in range(i+1, n):
                res = max(res, len(adjList[i]) + len(adjList[j]) - (i in adjList[j]))
        
        return res