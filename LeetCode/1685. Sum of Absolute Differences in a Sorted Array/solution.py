class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        total_sum = sum(nums)
        left_sum = 0


        for i in range(n):
            right_sum = total_sum - nums[i] - left_sum
            left_elements = i
            right_elements = n - i - 1
            ans.append(
                left_elements*nums[i] - left_sum +
                right_sum - right_elements*nums[i]
            )
            left_sum += nums[i]
       
        return ans
