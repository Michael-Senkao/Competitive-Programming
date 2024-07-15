class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def long(s):
            if len(s) < 2:
                return ""
            
            sset = set(s)
            for i in range(len(s)):
                ch = s[i]
                if ch.swapcase() not in s:
                    s1 = long(s[:i])
                    s2 = long(s[i+1: ])
                    return s1 if len(s1) >= len(s2) else s2
            return s

        return long(s)

