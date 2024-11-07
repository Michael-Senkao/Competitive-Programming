class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_cols = len(bin(max(candidates)))
        bits = [(max_cols - len(bin(num)))*'0' + bin(num) for num in candidates]
        result = 0

        for c in range(2,max_cols):
            temp = 0
            for r in range(len(candidates)):
                temp += bits[r][c] == '1'
            result = max(result, temp)
        return result