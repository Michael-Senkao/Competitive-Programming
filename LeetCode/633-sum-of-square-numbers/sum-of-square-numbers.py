from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start,end = 0, int(sqrt(c))
        print(start, end)
        while start <= end:
            if start**2+end**2 == c:
                return True
            if start**2 + end**2 < c:
                start +=1
            else:
                end-=1

        return False