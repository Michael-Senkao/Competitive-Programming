class Solution:
    def makeFancyString(self, s: str) -> str:
        
        n = len(s)
        if n < 3:
            return s

        res = [s[0]]
        count = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                res.append(s[i])

        return ''.join(res)
        