class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        length = n + len(rolls)
        total = length*mean
        curr_sum = sum(rolls)
        rem_sum = total - curr_sum

        if rem_sum < n or rem_sum > n*6:
            return []

        rem_sum -= n
        res = []
        for _ in range(n):
            val = min(1 + rem_sum, 6)
            res.append(val)
            rem_sum -= val - 1
        return res