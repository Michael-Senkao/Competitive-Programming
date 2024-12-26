class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dp(index, curr_sum):
            if index == n:
                if curr_sum == target:
                    return 1
                return 0
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            sub = dp(index + 1, -nums[index] + curr_sum)
            add = dp(index + 1, nums[index] + curr_sum)

            memo[(index, curr_sum)] = add + sub
            return memo[(index, curr_sum)]

        n = len(nums)
        
        return dp(0,0)


