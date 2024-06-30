class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, city):
        if city == self.parent[city]:
            return city
        return self.find(self.parent[city])
    def union(self, city1, city2):
        root1 = self.find(city1)
        root2 = self.find(city2)
        if root1 != root2:
            self.parent[root2] = root1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        x = UnionFind(n)
        province = set()
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    x.union(i, j)
        print(x.parent)
        for p in x.parent:

            province.add(x.find(p))
        return len(province)