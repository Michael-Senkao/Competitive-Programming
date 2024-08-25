class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        left_min = []
        curr_min = float("inf")

        for num in nums:
            left_min.append(curr_min)
            curr_min = min(curr_min, num)

        curr_max = float("-inf")
        for i in range(n-1, -1, -1):
            if left_min[i] < nums[i] < curr_max:
                return True
            curr_max = max(curr_max, nums[i])
        
        return False
