class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        def complement(a) -> str:
            return 1 if a == 0 else 0

        n = len(nums)
        flips = [0]*n
        res = 0

        # If first bit is '0' we will need atleast one flip
        if nums[0] == 0:
            flips[0] += 1
            nums[0] = 1
            res = 1
            if k < n:
                flips[k] = -1
        
        # Use range sum to calculate the total flips for each bit
        for i in range(1,n):
            flips[i] += flips[i-1] # Find prefix sum of flips at index i
            
            if flips[i] & 1: 
                nums[i] = complement(nums[i]) # If flips is ODD the current bit changes
            if nums[i] == 0:
                # current bit is not set we need a flip to set it 
                res += 1
                if i + k > n:
                    return -1 # Less tahn k bits in the range
                flips[i] += 1
                if i + k < n:
                    flips[i+k] -= 1
        
        
        return res