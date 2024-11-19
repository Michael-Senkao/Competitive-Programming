class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        found = set()
        left = 0
        max_sum = curr_sum = 0
        for right in range(len(nums)):
            while found and  nums[right] in found:
                found.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
        
            found.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[left]
                found.remove(nums[left])
                left += 1

        return max_sum