class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        res = 0

        i = 0
        while i < n:
            ch = s[i]
            curr_len = 1
            i += 1
            while i < n and s[i] == ch:
                curr_len += 1
                i += 1

            for j in range(curr_len):
                count[(ch, j + 1)] += (curr_len - j)

        for key,val in count.items():
            if val > 2:
                res = max(res, key[1])
        return res if res > 0 else -1
        