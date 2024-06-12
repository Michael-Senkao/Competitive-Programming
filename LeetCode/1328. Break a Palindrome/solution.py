class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
            
        i = 0
        mid = n//2
        while i < mid and palindrome[i] == 'a':
            i+=1
       
        if i < mid:
            return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:n-1] + 'b'
