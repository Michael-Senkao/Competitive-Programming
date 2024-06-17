class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
        res = []
        subset = []
        n = len(candidates)

        def backtrack(index):
            subset_sum = sum(subset)
            if subset_sum == target:
                res.append(subset[::])
                return
            if index >= n or subset_sum > target:
                return
            subset.append(candidates[index])
            backtrack(index)
            subset.pop()
            backtrack(index + 1)

        backtrack(0)

        return res