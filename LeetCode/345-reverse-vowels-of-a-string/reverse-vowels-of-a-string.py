class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right = 0, len(s) - 1
        result = [""]*len(s)
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}

        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                result[left],result[right] = s[right],s[left]
                left += 1
                right -= 1
            elif s[left] in vowels:
                result[right] = s[right]
                right -= 1
            elif s[right] in vowels:
                result[left] = s[left]
                left += 1
            else:
                result[left],result[right] = s[left],s[right]
                left += 1
                right -= 1
        return "".join(result)

        