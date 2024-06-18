class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def backtrack(index, current, total):
            if total == target:
                res.append(current)
                return
            if index >= n or total > target:
                return
            backtrack(index + 1, current + [candidates[index]], total + candidates[index])
            while index + 1 < n and candidates[index + 1] == candidates[index]:
                index += 1
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)
        return res
