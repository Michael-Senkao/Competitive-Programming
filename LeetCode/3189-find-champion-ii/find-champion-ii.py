class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = set([i for i in range(n)])

        for _,w in edges:
            if w in teams:
                teams.remove(w)
        if len(teams)>1:
            return -1
        for t in teams:
            return t