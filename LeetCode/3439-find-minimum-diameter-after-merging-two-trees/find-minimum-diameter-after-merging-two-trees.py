class Solution:
    def createGraph(self,edges):
        graph = defaultdict(list)
        n =-1
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            n = max(n,a,b)
        n+=1
        degree = [0] * n
        for a,b in edges:
            degree[a]+=1
            degree[b]+=1
        return (graph,degree,n)
    def findDiameter(self, graph,degree,n):
        diameter = 0
        q = deque()
        for key,value in enumerate(degree):
            if value == 1:
                q.append(key)
        distance = [0]*n
        while n > 2:
            node = q.popleft()
            for nei in graph[node]:
                degree[nei]-=1
                distance[nei]=max(distance[nei],distance[node]+1)
                if degree[nei] == 1:
                    q.append(nei)
            n-=1
        if n == 2:
            diameter = distance[q[0]] + distance[q[1]] + 1
        elif n == 1:
            diameter = 2*distance[q[0]]
        return diameter

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        graph1,degree1,n1 = self.createGraph(edges1)
        graph2,degree2,n2 = self.createGraph(edges2)
        diameter1 = self.findDiameter(graph1,degree1,n1)
        diameter2 = self.findDiameter(graph2,degree2,n2)

        return max(diameter1,diameter2,(ceil(diameter1/2)+ceil(diameter2/2))+1)