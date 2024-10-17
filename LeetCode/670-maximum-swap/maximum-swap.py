class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        s1 = s2 = max_i =n - 1

        for i in range(n-1, -1, -1):
            if nums[i] > nums[max_i]:
                max_i = i
                
            if nums[i] < nums[max_i]:
                s1,s2 = i, max_i

        nums[s1],nums[s2] = nums[s2], nums[s1]
        return int("".join(nums))
        