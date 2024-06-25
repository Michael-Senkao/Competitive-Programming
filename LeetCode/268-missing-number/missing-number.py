class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def cyclic_sort(nums):
            i = 0
            n = len(nums)
            for i in range(n):
                index = nums[i]
                while index != i and index < n:
                    nums[i],nums[index] = nums[index],nums[i]
                    index = nums[i]

        n = len(nums)
        cyclic_sort(nums)
        for i in range(n):
            if nums[i] != i:
                return i
        return n