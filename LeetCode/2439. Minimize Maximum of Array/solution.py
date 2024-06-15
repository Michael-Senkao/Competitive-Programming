class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        total = nums[0]

        for i in range(1,n):
            total += nums[i]
            average = ceil(total / (i + 1))
            res = max(res, average)

        return res
