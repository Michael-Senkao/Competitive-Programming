class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        def findLongest(left, right):
            while left >=0 and right < n:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            if len(self.res) < right - left - 1:
                self.res = s[left + 1: right]

        n = len(s)
        self.res = ""
        for i in range(n):
            findLongest(i,i)
            findLongest(i,i-1)

        return self.res