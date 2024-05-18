class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total_ones = s.count('1')
        ans = 0

        current_zeros = current_ones = 0
        for i in range(n-1):
            if s[i] == '0':
                current_zeros += 1
            else:
                current_ones += 1
            ans = max(ans, current_zeros + total_ones - current_ones)
        return ans
