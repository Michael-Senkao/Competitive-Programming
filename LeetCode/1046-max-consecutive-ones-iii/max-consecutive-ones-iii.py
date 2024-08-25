class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        zeros = 0
        left = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
                if zeros > k:
                    while nums[left] != 0:
                        left += 1

                    left += 1
                    zeros -= 1
    
            result = max(result, right - left + 1)
        
        return result
        