class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        canReach = set()
        res = []

        for u,v in edges:
            canReach.add(v)

        for i in range(n):
            if i not in canReach:
                res.append(i)
        return res
