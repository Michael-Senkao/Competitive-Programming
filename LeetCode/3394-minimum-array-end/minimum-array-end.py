class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bit_mask = n - 1
        res = 0
        pw = 0
        while x:
            if x & 1 == 0:
                res = ((2**pw)*(bit_mask & 1)) + res
                # print(res)
                bit_mask >>= 1
            else:
                res = ((2**pw)*(x & 1)) + res
            x >>= 1
            pw+=1
        while bit_mask:
            res = ((2**pw)*(bit_mask & 1)) + res
            # print(res)
            bit_mask >>= 1
            pw += 1
        return res