class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0

        while target > 1 and maxDoubles > 0:
            res += 1
            if target & 1:
                target -= 1
            else:
                target >>= 1
                maxDoubles -= 1
      
        res += (target-1)
        return res
