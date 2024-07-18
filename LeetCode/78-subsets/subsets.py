class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, subset):
            if index >= n:
                res.append(subset)
                return
            
            backtrack(index + 1, subset + [nums[index]])
            backtrack(index + 1, subset)
        

        res = []
        n = len(nums)
        backtrack(0, [])
        return res