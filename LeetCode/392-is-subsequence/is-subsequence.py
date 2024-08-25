class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False

        i = 0
        j = 0
        
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1

        return j == len(s)
        

            
        