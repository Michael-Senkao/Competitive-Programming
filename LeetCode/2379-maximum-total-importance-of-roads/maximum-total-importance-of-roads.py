class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0]*n
        res = 0

        for a,b in roads:
            degrees[a] += 1
            degrees[b] += 1

        degrees.sort()
        for i in range(n):
            res += degrees[i]*(i+1)
        return res