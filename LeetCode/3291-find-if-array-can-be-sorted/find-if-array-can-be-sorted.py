class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        prev_bit,prev_min,prev_max = 0,0,0
        c_min,c_max,c_bit = nums[0],nums[0],nums[0].bit_count()
        n = len(nums)
        for i in range(1,n):
            if nums[i].bit_count()==c_bit:
                c_max = max(c_max,nums[i])
                c_min = min(c_min,nums[i])
            elif c_min >= prev_max:
                prev_max = c_max
                prev_min = c_min
                prev_bit = c_bit
                c_min,c_max,c_bit = nums[i],nums[i],nums[i].bit_count()
            else:
                return False
        return c_min >= prev_max