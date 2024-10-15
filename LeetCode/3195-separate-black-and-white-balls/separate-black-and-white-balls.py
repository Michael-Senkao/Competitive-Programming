class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        ans = 0

        for ch in s:
            if ch == '0':
                ans += ones
            else:
                ones += 1
        return ans
        