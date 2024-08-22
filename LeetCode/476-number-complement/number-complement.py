class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        mul = 1
        while num > 0:
            bit = (num&1) ^ 1
            result += bit*mul
            mul*=2
            num >>= 1
        return result
        