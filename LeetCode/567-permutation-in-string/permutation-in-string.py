class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        n1,n2 = len(s1), len(s2)
        frq1 = [0]*26
        window = [0]*26
        count = n1
        
        for i in range(n1):
            frq1[ord(s1[i]) - 97] += 1
            window[ord(s2[i]) - 97] += 1
        
        if frq1 == window:
            return True
        for i in range(n1, n2):
            window[ord(s2[i]) - 97] += 1
            
            window[ord(s2[i - n1]) - 97] -= 1
            if frq1 == window:
                return True


        return False