class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_set_bit(num):
            count = 0
            while num > 0:
                count += num&1
                num >>= 1
            return count
        res = []
        i = 0
        while i <= n:
            res.append(count_set_bit(i))
            i += 1
        
        return res