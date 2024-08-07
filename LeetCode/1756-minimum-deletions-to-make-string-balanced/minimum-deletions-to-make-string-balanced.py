class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_as = 0
        a_count = b_count = 0

        
        res = float('inf')
        for ch in s:
            if ch == 'a':
                total_as += 1
        
        for i in range(len(s)):
            if s[i] == 'a':
                a_count += 1
            right_as = total_as - a_count
           
            res = min(res, right_as + b_count)
            if s[i] == 'b':
                b_count += 1

        return res