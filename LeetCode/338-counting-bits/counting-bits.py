class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_set_bit(num):
            count = num&1
            num >>= 1
            return count + res[num]
        res = [0]
        i = 1
        while i <= n:
            res.append(count_set_bit(i))
            i += 1
        
        return res