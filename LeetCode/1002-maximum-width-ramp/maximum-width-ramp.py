class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        n = len(nums)
        res = 0

        for i in range(n):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)

        i = n - 1
        while stack:
            if nums[i] >= nums[stack[-1]]:
                res = max(res, i - stack[-1])
                stack.pop()
            else:
                i -= 1
        return res
        