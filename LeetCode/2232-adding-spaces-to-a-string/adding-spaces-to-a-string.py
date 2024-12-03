class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        i = 0
        size = len(s)
        for j in range(len(spaces)):
            while i < spaces[j]:
                res.append(s[i])
                i+=1
            res.append(' ')
        while i < size:
            res.append(s[i])
            i+=1
        return ''.join(res)