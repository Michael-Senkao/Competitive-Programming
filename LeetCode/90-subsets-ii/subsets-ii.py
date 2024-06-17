class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        
        def dfs(index):
            if index >= n:
                res.append(subset.copy())
                return
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            while index+1 < n and nums[index+1] == nums[index]:
                index += 1
            dfs(index + 1)

        nums.sort()
        dfs(0)
        return res