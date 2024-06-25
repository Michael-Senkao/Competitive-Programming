class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def cyclic_sort(nums, n):
            for i in range(n):
                index = nums[i] - 1
                while index != i and nums[index] != index + 1:
                    nums[index],nums[i] = nums[i],nums[index]
                    index = nums[i] - 1

        n = len(nums)
        res = []
        cyclic_sort(nums, n)

        for i in range(n):
            if nums[i] != i + 1:
                res.append(i+1)
        
        return res
