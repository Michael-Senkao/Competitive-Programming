class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        postfix_sum = [0]*n 
        total_sum = 0

        # Backward pass
        for i in range(-1, -1*n - 1, -1):
            total_sum += nums[i]
            postfix_sum[i] = total_sum

        # Forward pass
        total_sum = 0
        for i in range(n):
            total_sum += nums[i]
            if total_sum == postfix_sum[i]:
                return i
        
        return -1
