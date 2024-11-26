class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        can_beat = [0]*n
        champ = -1

        for _,w in edges:
            can_beat[w]+= 1
        for i in range(n):
            if not can_beat[i]:
                if champ != -1:
                    return -1
                champ = i

        return champ