class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo = {}
        @cache
        def dp(index, curr_value):
            if index == len(nums):
                return 1 if curr_value == target else 0
            
            # Check if the result is already computed
            # if (index, curr_value) in memo:
            #     return memo[(index, curr_value)]
            
            # Calculate the number of ways by adding and subtracting the current number
            add = dp(index + 1, curr_value + nums[index])
            subtract = dp(index + 1, curr_value - nums[index])
            
            # Store the result in the memo dictionary
            # memo[(index, curr_value)] = add + subtract
            # return memo[(index, curr_value)]
            return add + subtract
        
        return dp(0, 0)
