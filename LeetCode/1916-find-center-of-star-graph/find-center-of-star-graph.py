class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        a,b = set(edges[0]), set(edges[1])

        return list(a.intersection(b))[0]