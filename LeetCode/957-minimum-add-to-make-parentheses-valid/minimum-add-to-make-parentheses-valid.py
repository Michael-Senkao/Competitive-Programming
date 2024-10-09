class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = unbalanced = 0
        for ch in s:
            if ch == '(':
                open_brackets += 1
            elif open_brackets > 0:
                open_brackets -= 1
            else:
                unbalanced += 1
        return open_brackets + unbalanced