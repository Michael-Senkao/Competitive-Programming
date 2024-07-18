class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, subset):
            if index >= n:
                res.append(subset)
                return
            
            backtrack(index + 1, subset + [nums[index]])
            index += 1
            while index < n and nums[index]== nums[index-1]:
                index += 1
            backtrack(index, subset)
        
       
        res = []
        n = len(nums)
        nums.sort()
        backtrack(0, [])
        return res