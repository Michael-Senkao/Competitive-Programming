class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Initialize a dp list where each element starts with a value of 1.
        # This represents the length of the longest increasing subsequence ending at each index.
        dp_left = [1] * n
        dp_right = [1] * n

        # Iterate through each element in the nums list from the second element onward
        for i in range(1, n):
            # For each element nums[i], check all previous elements nums[j] with j < i
            for j in range(i):
                # If nums[i] is greater than nums[j], we can extend the increasing subsequence ending at j
                if nums[i] > nums[j]:
                    # Update dp[i] to be the maximum of its current value and dp[j] + 1
                    # This ensures dp[i] reflects the length of the longest increasing subsequence ending at i
                    dp_left[i] = max(dp_left[i], dp_left[j] + 1)

        # Iterate through each element in the nums list from the second element onward
        for i in range(n - 2, -1, -1):
            # For each element nums[i], check all previous elements nums[j] with j < i
            for j in range(n-1, i, -1):
                # If nums[i] is greater than nums[j], we can extend the increasing subsequence ending at j
                if nums[i] > nums[j]:
                    # Update dp[i] to be the maximum of its current value and dp[j] + 1
                    # This ensures dp[i] reflects the length of the longest increasing subsequence ending at i
                    dp_right[i] = max(dp_right[i], dp_right[j] + 1)
        max_mountain = 0
        for i in range(1, n - 1):
            if dp_left[i] > 1 and dp_right[i] > 1:
                max_mountain = max(max_mountain, dp_right[i] + dp_left[i] - 1)
        # Return the maximum value in dp, representing the length of the longest increasing subsequence in nums
        # print(dp_left)
        # print(dp_right)
        return n - max_mountain