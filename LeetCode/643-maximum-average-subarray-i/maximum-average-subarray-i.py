class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        window_sum = 0
        result = float("-inf")

        for i in range(k-1):
            window_sum += nums[i]

        for right in range(k - 1, n):
            window_sum += nums[right]
            result = max(result, window_sum)
            window_sum -= nums[left]
            left += 1
            right += 1

        return result / k
        