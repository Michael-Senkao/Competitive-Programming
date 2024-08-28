class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            runningSum = max(num, num + runningSum)
            max_sum = max(max_sum, runningSum)
        return max_sum
