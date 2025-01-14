class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        found = [0]*(n+1)
        res = []
        prefix = 0

        for i in range(n):
            found[A[i]] += 1
            if found[A[i]] == 2:
                prefix += 1
                
            found[B[i]] += 1
            if found[B[i]] == 2:
                prefix += 1
            
            
            res.append(prefix)

        return res