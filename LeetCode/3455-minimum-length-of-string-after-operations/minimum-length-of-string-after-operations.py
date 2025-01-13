class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        res = 0

        for val in freq.values():
            if val & 1:
                res += 1
            else:
                res += 2

        return res