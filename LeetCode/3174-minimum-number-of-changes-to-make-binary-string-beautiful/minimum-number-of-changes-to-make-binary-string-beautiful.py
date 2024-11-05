class Solution:
    def minChanges(self, s: str) -> int:
        min_change = 0

        for i in range(1,len(s),2):
            if s[i] != s[i-1]:
                min_change += 1

        return min_change