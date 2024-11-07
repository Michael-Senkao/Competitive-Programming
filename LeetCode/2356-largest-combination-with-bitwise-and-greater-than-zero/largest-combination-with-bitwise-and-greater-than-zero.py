class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0]*24

        for num in candidates:
            i = 7
            while num:
                bits[i] += num & 1
                num >>= 1
                i -= 1
        
        return max(bits)