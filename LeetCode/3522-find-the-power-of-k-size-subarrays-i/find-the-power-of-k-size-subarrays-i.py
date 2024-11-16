class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums

        l = 0
        sorted_size = 0
        res = []
        for r in range(1, n):
            if nums[r] != nums[r-1] + 1:
                while l < r and l+k <= n:
                    res.append(-1)
                    l += 1
           
            if (r - l + 1) == k:
                res.append(nums[r])
                l += 1

        return res