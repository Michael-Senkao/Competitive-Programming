class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(current, index):
            if index == n:
                res.append(current)
                return 
            
            backtrack(current + [nums[index]], index + 1)
            backtrack(current, index + 1)

        backtrack([], 0)
        return res