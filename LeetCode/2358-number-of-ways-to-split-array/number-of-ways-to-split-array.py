class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        count = 0
        n = len(nums)
        left_sum = 0
        for i in range(n-1):
            left_sum += nums[i]
            right_sum -= nums[i]
            count += (left_sum >= right_sum)
        return count