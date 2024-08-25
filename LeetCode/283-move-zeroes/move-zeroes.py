class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zero = 0

        for index in range(n):
            if nums[index] == 0:
                while non_zero < n and (nums[non_zero] == 0 or non_zero < index):
                    non_zero += 1
                if non_zero < n:
                    nums[index], nums[non_zero] = nums[non_zero],0
                else:
                    return
        