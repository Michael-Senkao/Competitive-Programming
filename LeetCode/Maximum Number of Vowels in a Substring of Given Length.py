'''
QUESTION:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u'] 
        n = len(s)
        left = 0
        right = 0
        window_vowels = 0

        # Get no. of vowels in window of size k
        while right < k:
            if s[right] in vowels:
                window_vowels += 1

            right += 1

        ans = window_vowels

        # Slide and shrink the window towards the end of s, while tracking the vowels
        while right < n:
            if s[right] in vowels:
                window_vowels += 1    
            if s[left] in vowels:
                window_vowels -= 1    

            right += 1
            left += 1
            ans = max(ans, window_vowels)

        return ans
