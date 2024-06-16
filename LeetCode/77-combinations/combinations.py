class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(current, i):
            nonlocal res
            if len(current) == k:
                res.append(current)
                return
            if i <= n:
                backtrack(current + [i], i+1)
                backtrack(current, i+1)

        res = []
        backtrack([], 1)
        return res