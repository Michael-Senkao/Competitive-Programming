class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_cols = len(bin(max(candidates))[2:])
        bits = [(max_cols - len(bin(num)[2:]))*'0' + bin(num)[2:] for num in candidates]
        result = 0

        for c in range(max_cols):
            temp = 0
            for r in range(len(candidates)):
                temp += bits[r][c] == '1'
            result = max(result, temp)
        return result