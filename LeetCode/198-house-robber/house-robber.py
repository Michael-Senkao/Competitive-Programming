class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            memo[index] = max(dp(index+1), dp(index+2) + nums[index])
           
            return memo[index]

        n = len(nums)
        memo = {}
        
        return dp(0)