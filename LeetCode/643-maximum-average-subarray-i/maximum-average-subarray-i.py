class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left,right = 0, k - 1
        window_sum = sum(nums[:k-1])
        result = float("-inf")

        while right < n:
            window_sum += nums[right]
            result = max(result, window_sum)
            window_sum -= nums[left]
            left += 1
            right += 1

        return result / k
        