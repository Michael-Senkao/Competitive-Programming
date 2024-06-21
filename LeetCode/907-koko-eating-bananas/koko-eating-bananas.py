class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def can_finish(k):
            i = 0
            count = 0
            while i < n and count <= h:
                count += ceil(piles[i]/k)
                i += 1
            return i>=n and count <= h
        
        l,r = 1, max(piles)

        while l < r:
            mid = l + (r - l)//2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1

        return l