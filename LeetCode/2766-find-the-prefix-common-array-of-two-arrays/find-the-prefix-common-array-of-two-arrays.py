class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        found = [False]*(n+1)
        res = []
        prefix = 0

        for i in range(len(A)):
            if found[A[i]]:
                prefix += 1
            else:
                found[A[i]] = True
            if found[B[i]]:
                prefix += 1
            else:
                found[B[i]] = True
            
            res.append(prefix)

        return res