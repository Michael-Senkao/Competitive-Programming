class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        n = len(nums)
        current = 0
        for i in range(n-1):
            current += nums[i]
            count += (current >= (total - current))
        return count