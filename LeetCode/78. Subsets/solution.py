class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
    
        for i in range(n):
            m = len(res)
            for j in range(m):
                res.append(res[j] + [nums[i]])
            
        return res
