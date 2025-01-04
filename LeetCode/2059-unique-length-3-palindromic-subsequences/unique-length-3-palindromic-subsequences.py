class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        unique_right = Counter(s)
        unique_left = set()

        palindromes = set()
        for i in range(n):
            unique_right[s[i]] -= 1
            if unique_right[s[i]] == 0:
                del unique_right[s[i]]
                
            for char in unique_left:
                if char in unique_right:
                    palindromes.add(char + s[i] + char)
            unique_left.add(s[i])

        return len(palindromes)
        