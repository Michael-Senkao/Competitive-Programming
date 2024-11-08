class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        total_xor = reduce(lambda x,y: x ^ y,nums)
        max_num = (1 << maximumBit) - 1
        n = len(nums)
        res = [0]*n
        
        for i in range(n-1,-1,-1):
            res[n - i - 1] = total_xor ^ max_num
            total_xor ^= nums[i]
    
        return res