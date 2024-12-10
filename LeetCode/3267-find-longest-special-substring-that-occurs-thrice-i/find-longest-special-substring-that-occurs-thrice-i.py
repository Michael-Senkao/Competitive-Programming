class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        res = 0

        i = 0
        while i < n:
            curr_str = [s[i]]
            i += 1
            while i < n and s[i] == s[i-1]:
                curr_str.append(s[i])
                i += 1

            temp = []
            for j in range(len(curr_str)):
                temp.append(curr_str[j])
                count["".join(temp)] += (len(curr_str) - j)

        for key,val in count.items():
            if val > 2:
                res = max(res, len(key))
        return res if res > 0 else -1
        