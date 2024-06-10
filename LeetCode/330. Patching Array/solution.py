class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        upper,cost,i = 0,0,0


        while upper < n:
            if i < len(nums) and nums[i] <= upper + 1:
                upper += nums[i]
                i += 1
            else:
                cost += 1
                upper += upper + 1

        return cost
