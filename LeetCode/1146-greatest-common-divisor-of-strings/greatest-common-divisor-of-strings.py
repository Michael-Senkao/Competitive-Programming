class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1,n2 = len(str1), len(str2)
        gcd = ""
        if n2 < n1:
            str1,str2 = str2, str1
            n1,n2 = n2,n1

        i = 0
        prefix = ""
        while i < n1:
            prefix += str1[i]
            if n1 % len(prefix) == 0 and n2 % len(prefix) == 0:
                if ((prefix * (n1//len(prefix))) == str1) and ((prefix * (n2//len(prefix))) == str2):
                    gcd = prefix
            i += 1
        return gcd
