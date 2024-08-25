class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        window_vowels = 0
        result = 0

        for i in range(k - 1):
            if s[i] in vowels:
                window_vowels += 1
        
        left = 0

        for right in range(k-1, n):
            if s[right] in vowels:
                window_vowels += 1

            result = max(result, window_vowels)

            if s[left] in vowels:
                window_vowels -= 1
            left += 1

        return result
        