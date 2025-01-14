class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        countA,countB = set(),set()
        res = []

        for i in range(len(A)):
            countA.add(A[i])
            countB.add(B[i])

            count = 0
            for num in countB:
                if num in countA:
                    count += 1
            
            res.append(count)

        return res