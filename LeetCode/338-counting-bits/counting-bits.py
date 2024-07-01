class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0]
        i = 1
        while i <= n:
            res.append((i&1) + res[i>>1])
            i += 1
        
        return res