class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_len = 0     
        for x in arr:
            if x - difference in dp:
                dp[x] = dp[x - difference] + 1
            else:
                dp[x] = 1
            
            max_len = max(max_len, dp[x])
        
        return max_len
