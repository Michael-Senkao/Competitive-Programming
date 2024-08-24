class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        prefix = 1
        for num in nums:
            result.append(prefix)
            prefix *= num
        
        sufix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= sufix
            sufix *= nums[i]

        return result

        