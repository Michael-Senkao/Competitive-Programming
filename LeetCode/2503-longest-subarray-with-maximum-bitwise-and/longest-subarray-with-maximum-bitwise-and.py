class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_k = max(nums)
        n = len(nums)

        # for i in range(1, n):
        #     k = max(k & nums[i], nums[i])
        #     max_k = max(max_k, k)
        
        # print(max_k)
        i = 0
        ans = 0
        while i < n:
            count = 0
            while i < n and nums[i] == max_k:
                count += 1
                i += 1
            i += 1
            ans = max(ans, count)
        return ans
        