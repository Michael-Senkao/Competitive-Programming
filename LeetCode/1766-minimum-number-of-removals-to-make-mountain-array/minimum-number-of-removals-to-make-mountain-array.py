class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp_left = [1] * n
        dp_right = [1] * n
        # LIS from left to right
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_left[i] = max(dp_left[i], dp_left[j] + 1)

        # LIS from right + left
        for i in range(n - 2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    dp_right[i] = max(dp_right[i], dp_right[j] + 1)
        max_mountain = 0
        for i in range(1, n - 1):
            if dp_left[i] > 1 and dp_right[i] > 1:
                max_mountain = max(max_mountain, dp_right[i] + dp_left[i] - 1)
    

        return n - max_mountain