class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left,n = 0, len(s)
        res = 0

        for right in range(n):
            ch = s[right]
            while ch in char_set:
                char_set.discard(s[left])
                left += 1
            char_set.add(ch)
            res = max(res, len(char_set))

        return res