class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def cyclic_sort(nums, n):
            for i in range(n):
                index = nums[i] - 1
                while index != i and nums[index] != index + 1:
                    nums[i],nums[index] = nums[index],nums[i]
                    index = nums[i] - 1

        n = len(nums)
        cyclic_sort(nums, n)
        return nums[-1]