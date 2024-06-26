class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def cyclic_sort(nums, n):
            for i in range(n):
                index = nums[i] - 1
                while 0 <= index < n and index != i and nums[index] != index + 1:
                    nums[index],nums[i] = nums[i],nums[index]
                    index = nums[i] - 1

        
        n = len(nums)
        cyclic_sort(nums, n)
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n + 1
