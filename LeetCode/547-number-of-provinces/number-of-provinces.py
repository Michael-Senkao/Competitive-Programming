class UnionFind:
    def __init__(self, size):
        self.root = {i:i for i in range(size)}
        self.rank = [0]*size

    def find(self, node):
        if self.root[node] == node:
            return node
        return self.find(self.root[node])
    
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.root[parent_b] = parent_a
            elif self.rank[parent_b] > self.rank[parent_a]:
                self.root[parent_a] = parent_b
            else:
                self.root[parent_b] = parent_a
                self.rank[parent_a] += 1
        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        x = UnionFind(n)
        province = set()
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    x.union(i, j)
        print(x.root)
        for node,parent in x.root.items():
            province.add(x.find(parent))
        return len(province)