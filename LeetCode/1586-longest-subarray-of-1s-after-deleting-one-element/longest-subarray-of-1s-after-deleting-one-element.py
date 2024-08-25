class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        has_zero = False
        left = 0
        result = 0

        for right in range(n):
            if nums[right] == 0:
                if has_zero:
                    while nums[left] != 0:
                        left += 1
                    
                    left += 1
                else:
                    has_zero = True
            result = max(result, right - left)
            
        return result
        