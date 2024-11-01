class Solution:
    def makeFancyString(self, s: str) -> str:
        
        n = len(s)
        if n < 3:
            return s

        res = [s[0], s[1]]
        for i in range(2, n):
            if not(s[i] == s[i-1] and s[i] == s[i - 2]):
                res.append(s[i])

        return ''.join(res)
        