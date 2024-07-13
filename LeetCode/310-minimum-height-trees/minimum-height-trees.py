class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        edge_count = {}
        leaves = deque()

        for node,neighbors in adjList.items():
            if len(neighbors) == 1:
                leaves.append(node)
            edge_count[node] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                curr = leaves.popleft()
                n -= 1
                for neighbor in adjList[curr]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)